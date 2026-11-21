import os
# Room renderer with door (spawn tile) and furniture, following the client's wall/tile/door rules.
import sys, json
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from PIL import Image
import avatar as AV
from room import rt, hexrgb
F=os.environ.get('OH_FURNI','furni/')  # unzipped furniture folders (sheet.json + sprite.png)
def iso(x,z): return ((x-z)*24,(x+z)*12)
def wall_img(d,height=102):
    top=rt('wall-%s-top'%d); mid=rt('wall-%s-mid'%d); bot=rt('wall-%s-bottom'%d)
    mh=height-15+2
    im=Image.new('RGBA',(30,15+mh+bot.height),(0,0,0,0)); im.alpha_composite(top,(0,0))
    m=Image.new('RGBA',(30,mh),(0,0,0,0)); m.alpha_composite(mid.crop((0,0,30,1)),(0,0))
    row=mid.crop((0,1,30,2))
    for yy in range(1,mh-1): m.alpha_composite(row,(0,yy))
    m.alpha_composite(mid.crop((0,2,30,3)),(0,mh-1))
    im.alpha_composite(m,(0,15)); im.alpha_composite(bot,(0,15+mh)); return im
def furni(d,n):
    s=json.load(open(F+d+'/sheet.json'))['frames'][n]['frame']; im=Image.open(F+d+'/sprite.png').convert('RGBA')
    return im.crop((s['x'],s['y'],s['x']+s['w'],s['y']+s['h']))
BOOTH=lambda: furni('teleports@telephone','north')
def render(x0,x1,D,spawn_z,floor,wall,avatars=(),booths=(),left_items=(),right_items=()):
    items=[]; W=hexrgb(wall)
    wx=AV.tint(wall_img('x'),W); wz=AV.tint(wall_img('z'),W); wb=AV.tint(rt('wall-b'),W); wdoor=AV.tint(wall_img('x',24),W)
    t0=AV.tint(rt('tile'),hexrgb(floor[0])); t1=AV.tint(rt('tile'),hexrgb(floor[1])); ts=AV.tint(rt('tile'),(0x2f,0x2f,0x2f))
    X,Y=iso(x0-1,spawn_z); items.append(((x0-1+spawn_z)*2+0.1,0,ts,(X,Y)))  # client: getZIndex(spawn, 0.1)
    for z in range(D):
        for x in range(x0,x1+1):
            X,Y=iso(x,z); zi=(x+z)*2
            if x==x0:
                if z==spawn_z: items.append((zi,0,wdoor,(X-5,Y-99)))
                else: items.append((zi,0,wx,(X-5,Y-99)))
            if z==0: items.append((zi,0,wz,(X+25,Y-99)))
            if x==x0 and z==0: items.append((zi,0.01,wb,(X+20,Y-102)))
            items.append((zi+0.1,0,t0 if (x+z)%2==0 else t1,(X,Y)))
    top=(x1+D)*2+1
    for (z,a,h,im) in left_items:
        X,Y=iso(x0,z); items.append((top,0,im,(X+a,Y+12-a//2-h-im.height)))
    for (x,a,h,im,bl) in right_items:
        X,Y=iso(x,0); items.append((top,0,im,(X+24+a,Y+a//2-h-bl)))
    for (x,z,im) in booths:
        X,Y=iso(x,z); items.append(((x+z)*2+0.3,0,im,(X+1,Y-73)))
    sh=AV.tex('shadow').copy(); p=sh.load()
    for yy in range(sh.height):
        for xx in range(sh.width):
            if p[xx,yy][3]: p[xx,yy]=(0,0,0,int(p[xx,yy][3]*0.2))
    for av in avatars:
        x,z,arm,skin=av[:4]; mir=len(av)>4 and av[4]
        X,Y=iso(x,z); items.append(((x+z)*2+0.4,0,sh,(X+11,Y+6)))
        im,(ox,oy)=AV.compose('north',arm=arm,skin=hexrgb(skin),with_origin=True)
        if mir: im=im.transpose(Image.FLIP_LEFT_RIGHT); ox=im.width-ox+2
        items.append(((x+z)*2+0.5,0,im,(X+25-ox,Y+12-oy)))
    minx=min(p[0] for *_,p in items); miny=min(p[1] for *_,p in items)
    maxx=max(p[0]+i.width for *_,i,p in items); maxy=max(p[1]+i.height for *_,i,p in items)
    out=Image.new('RGBA',(maxx-minx,maxy-miny),(0,0,0,0))
    for z,o,im,(X,Y) in sorted(items,key=lambda t:(t[0],t[1])): out.alpha_composite(im,(X-minx,Y-miny))
    return out
if __name__=='__main__':
    fl_l=furni('flags@pirate','east'); fl_r=furni('flags@pirate','north')
    po_l=furni('alpha@a-24','a-24-north'); po_r=furni('alpha@a-24','a-24-east')
    b=BOOTH()
    im=render(1,9,7,3,floor=('#a49f7e','#b2ad8e'),wall=sys.argv[2] if len(sys.argv)>2 else '#a6c9b8',
      avatars=[(3,5,'idle','#efcfb1'),(2,3,'arm_wave_0','#a8714a'),(4,3,'idle','#7a4a2e',1),(6,2,'idle','#d9a57a'),(7,4,'idle','#f6dcc8',1),(8,2,'arm_wave_0','#c98e62',1),(6,6,'idle','#efcfb1',1)],
      booths=[(2,0,b),(3,0,b),(9,0,b)],
      left_items=[(1,2,44,fl_l),(5,4,40,po_l)],
      right_items=[(5,4,44,po_r,32),(7,4,44,po_r,32),(4,0,52,fl_r,26)])
    im.save(sys.argv[1]); print(im.size)
