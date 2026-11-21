import os
import json, sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from PIL import Image
import avatar as AV
R=os.environ.get('OH_CLIENT_ASSETS','../../../../openhotel/app/openhotel/app/client/src/assets/')+'room/'
rs=Image.open(R+'room.png').convert('RGBA'); rf=json.load(open(R+'room.json'))['frames']
def rt(n):
    f=rf[n]['frame']; return rs.crop((f['x'],f['y'],f['x']+f['w'],f['y']+f['h']))
def hexrgb(h): h=h.lstrip('#'); return tuple(int(h[i:i+2],16) for i in (0,2,4))
def iso(x,z,y=0): return ((x-z)*24, (x+z)*12 - y*24)
def mid_slice(h):
    t=rt('wall-x-mid'); return t
def wall_img(d):
    top=rt('wall-%s-top'%d); mid=rt('wall-%s-mid'%d); bot=rt('wall-%s-bottom'%d)
    mh=102-15+2
    im=Image.new('RGBA',(30,15+mh+bot.height),(0,0,0,0))
    im.alpha_composite(top,(0,0))
    # nine slice vertical: 1 top, stretched middle, 1 bottom
    m=Image.new('RGBA',(30,mh),(0,0,0,0))
    m.alpha_composite(mid.crop((0,0,30,1)),(0,0))
    row=mid.crop((0,1,30,2))
    for yy in range(1,mh-1): m.alpha_composite(row,(0,yy))
    m.alpha_composite(mid.crop((0,2,30,3)),(0,mh-1))
    im.alpha_composite(m,(0,15)); im.alpha_composite(bot,(0,15+mh))
    return im
HEADS=[]
LAST={}
def render(W,D,floor=('#a49f7e','#b2ad8e'),wall='#c4d3dd',avatars=(),holes=(),extras=()):
    items=[]
    wx=AV.tint(wall_img('x'),hexrgb(wall)); wz=AV.tint(wall_img('z'),hexrgb(wall)); wb=AV.tint(rt('wall-b'),hexrgb(wall))
    t0=AV.tint(rt('tile'),hexrgb(floor[0])); t1=AV.tint(rt('tile'),hexrgb(floor[1]))
    for z in range(D):
        for x in range(W):
            if (x,z) in holes: continue
            X,Y=iso(x,z)
            if x==0: items.append(((x+z)*2,0,wx,(X-5,Y-99)))
            if z==0: items.append(((x+z)*2,0,wz,(X+25,Y-99)))
            if x==0 and z==0: items.append(((x+z)*2,0.01,wb,(X+20,Y-102)))
            items.append(((x+z)*2+0.1,0,t0 if (x+z)%2==0 else t1,(X,Y)))
    shadow=AV.tex('shadow'); sh=shadow.copy(); p=sh.load()
    for yy in range(sh.height):
        for xx in range(sh.width):
            r,g,b,a=p[xx,yy]
            if a: p[xx,yy]=(0,0,0,int(a*0.2))
    for av in avatars:
        x,z,d,arm,skin=av[:5]; mir=len(av)>5 and av[5]
        X,Y=iso(x,z)
        items.append(((x+z)*2+0.4,0,sh,(X+11,Y+6)))
        im,(ox,oy)=AV.compose(d,arm=arm,skin=hexrgb(skin),with_origin=True)
        if mir: im=im.transpose(Image.FLIP_LEFT_RIGHT); ox=im.width-ox+2
        items.append(((x+z)*2+0.5,0,im,(X+25-ox,Y+12-oy))); HEADS.append((X+25-ox+im.width//2,Y+12-oy))
    for (zz,im,pos) in extras: items.append((zz,0.2,im,pos))
    xs=[p[0] for *_,p in items]; ys=[p[1] for *_,p in items]
    minx=min(xs); miny=min(ys)
    maxx=max(p[0]+i.width for *_,i,p in items); maxy=max(p[1]+i.height for *_,i,p in items)
    out=Image.new('RGBA',(maxx-minx,maxy-miny),(0,0,0,0)); LAST['heads']=[(hx-minx,hy-miny) for hx,hy in HEADS]; HEADS.clear()
    for z,o,im,(X,Y) in sorted(items,key=lambda t:(t[0],t[1])):
        out.alpha_composite(im,(X-minx,Y-miny))
    return out
if __name__=='__main__':
    im=render(7,6,avatars=[(2,2,'north','idle','#efcfb1'),(3,4,'east','arm_wave_0','#a8714a'),(5,1,'north','idle','#7a4a2e')])
    bg=Image.new('RGBA',im.size,(40,40,48,255)); bg.alpha_composite(im)
    bg.resize((im.width*2,im.height*2),Image.NEAREST).save('room-test.png'); print(im.size)
