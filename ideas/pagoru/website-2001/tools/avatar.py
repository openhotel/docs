import os
import json, sys, yaml
from PIL import Image
B=os.environ.get('OH_CLIENT_ASSETS','../../../../openhotel/app/openhotel/app/client/src/assets/')+'character/'
sheet=Image.open(B+'character.png').convert('RGBA')
frames=json.load(open(B+'character.json'))['frames']
data=yaml.safe_load(open(B+'character.yml'))
CD={'NORTH':0,'WEST':1,'NORTH_EAST':2,'SOUTH_WEST':3,'NORTH_WEST':4}
ACT={'idle':0,'sit':1,'walk_0':2,'walk_1':3,'walk_2':4,'walk_3':5}
ARMACT={'idle':0,'arm_grab':1,'arm_drink':2,'arm_wave_0':3}
SIDE={'right':0,'left':1}
def tex(name):
    f=frames[name]['frame']; return sheet.crop((f['x'],f['y'],f['x']+f['w'],f['y']+f['h']))
def tint(im,rgb):
    px=im.load(); out=im.copy(); o=out.load()
    for y in range(im.height):
        for x in range(im.width):
            r,g,b,a=px[x,y]
            if a: o[x,y]=(r*rgb[0]//255,g*rgb[1]//255,b*rgb[2]//255,a)
    return out
def g(d,*ks):
    for k in ks:
        if d is None: return None
        d=d.get(k)
    return d
def compose(direction,action='idle',arm='idle',skin=(255,255,255),headdir=None,with_origin=False):
    dd=data[direction]; target=dd.get('target'); bscale=dd.get('scale')
    fr=dd['frames'][action]
    items=[]  # (z, order, texname, scale, pivot)
    tdir=(target or direction).upper()
    pos=fr['body']['position']; bp=g(fr,'body','pivot') or {}
    items.append((0,0,'0%d%d'%(CD[tdir],ACT[action]),bscale or 1,(bp.get('x',0),bp.get('y',0))))
    # head
    core=data.get(target) if target else None
    cfr=g(core,'frames',action)
    hp=(g(fr,'head','pivot','x') or 0)+(g(cfr,'head','pivot','x') or 0),(g(fr,'head','pivot','y') or 0)+(g(cfr,'head','pivot','y') or 0)
    hs=(core or {}).get('scale') or bscale or 1
    items.append((2,1,'2%d'%CD[tdir],hs,hp))
    for i,side in enumerate(['left','right']):
        key=side+'_arm'; ba=fr.get(key) or {}
        ca=dd['frames'].get(arm,{}).get(key) if arm!='idle' else None
        piv=((ba.get('pivot') or {}).get('x',0)+((ca or {}).get('pivot') or {}).get('x',0),(ba.get('pivot') or {}).get('y',0)+((ca or {}).get('pivot') or {}).get('y',0))
        sc=(ca or {}).get('scale') or ba.get('scale') or bscale or 1
        s=side
        if ba.get('target'): s='right' if 'right' in ba['target'] else 'left'
        if bscale==-1: s='left' if s=='right' else 'right'
        vis=(ca or {}).get('visible', ba.get('visible', True))
        z=(ca or {}).get('zIndex', ba.get('zIndex', 1))
        if vis is False: continue
        items.append((z,2+i,'1%d%d%d'%(CD[tdir],SIDE[s],ARMACT[arm]),sc,piv))
    items.sort(key=lambda t:(t[0],t[1]))
    W,H=80,90; ox,oy=40,80
    canvas=Image.new('RGBA',(W,H),(0,0,0,0))
    for z,o,name,sc,(px,py) in items:
        if name not in frames: print('missing',name,file=sys.stderr); continue
        t=tint(tex(name),skin)
        if sc==-1: t=t.transpose(Image.FLIP_LEFT_RIGHT); x0=-(t.width-px) if False else None
        # local u -> parent x = sc*(u - px) - pos.x ; for sc=-1 leftmost parent x = -(w-1-px)... use exact
        if sc==1: X=-px-pos['x']
        else: X=-(t.width-px)-pos['x']+1-1
        Y=-py-pos['y']
        canvas.alpha_composite(t,(ox+X,oy+Y))
    bb=canvas.getbbox()
    if with_origin: return canvas.crop(bb),(ox-bb[0],oy-bb[1])
    return canvas.crop(bb)
if __name__=='__main__':
    out=Image.new('RGBA',(8*60,2*90),(200,220,240,255))
    for i,d in enumerate(['north','north_east','east','south_east','south','south_west','west','north_west']):
        try:
            a=compose(d,skin=(240,200,160)); out.alpha_composite(a,(i*60+5,5))
            b=compose(d,arm='arm_wave_0',skin=(150,100,70)); out.alpha_composite(b,(i*60+5,95))
        except Exception as e: print(d,repr(e))
    out.resize((out.width*3,out.height*3),Image.NEAREST).save('avatars.png')
