#!/usr/bin/python
import footgen

nPads = 6
pw = 2.0
ph = 5.0
pPitch = 3.0
px = -((nPads-1)/2.0) * pPitch
py = -15.0
wCopp = 2.0 
hdelt = 5.0
hSize = 5.0
lhSize = 3.0
pin1Size = pw/2
clr = pin1Size/2

f = footgen.Footgen("6PAD_CABLE_GLAND","geda")
f.generator._silk_arc(px,py+ph/2+pin1Size+clr,pin1Size,pin1Size,0,360)
for i in range(nPads):
	f.add_pad("%d"%(i+1),px,py,pw,ph)
	px += pPitch
f.add_pin("0",-hdelt,0,lhSize,lhSize+wCopp)
f.add_pin("0",+hdelt,0,lhSize,lhSize+wCopp)
f.add_pin("0",0,-hdelt,hSize,hSize+wCopp)
f.add_pin("0",0,+hdelt,hSize,hSize+wCopp)

f.finish()

px = -((nPads-1)/2.0) * pPitch
py = 0

f = footgen.Footgen("6PAD_WO_CABLE_GLAND","geda")
f.generator._silk_arc(px,py+ph/2+pin1Size+clr,pin1Size,pin1Size,0,360)
for i in range(nPads):
	f.add_pad("%d"%(i+1),px,py,pw,ph)
	px += pPitch

f.finish()
