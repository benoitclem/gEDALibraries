#!/usr/bin/python
# -*- coding: utf8 -*-
import footgen

# 8 shield body pads [1-8] numbered counterclockwise

suph = 8.62
lefw = 12.1/2

b1w = 0.95
b1h = 2.17
b1x = -(lefw-b1w/2)
b1y = -(suph-b1h/2)

b2w = 1.05
b2h = 1.2
b2x = -(lefw-b2w/2)
b2y = -(suph-7.21)

b3w = 1.05
b3h = 0.9
b3x = -(lefw-b3w/2)
b3y = 0

b4w = 1.7
b4h = 1.03
b4x = -(lefw-3.65)
b4y = 5.43-b4h/2

b5w = 1.2
b5h = 0.88
b5x = 0
b5y = 5.43-b5h/2

b6w = 1.7
b6h = 1.03
b6x = lefw-3.65
b6y = 5.43-b6h/2

b7w = 0.88
b7h = 1.25
b7x = lefw-b7w/2
b7y = -(suph-5.425)

b8w = 1.19
b8h = 2.03
b8x = lefw-b8w/2
b8y = -(suph-b8h/2)

#  Pad stuffs
ppitch = 1.1
poff = 0.1
pw = 0.7
ph = 0.95
px = poff - 3*ppitch 
py = -(suph - 3.46 + ph/2)

# Outline stuffs
oclr = 0.25
ox = 0
oy = -1.6
ow = 12.1 + oclr*2
oh = 14.05 + oclr*2

f = footgen.Footgen("USD","geda")
# Body
for i in range(8):
	j = i+1
	f.add_pad("9", eval("b%dx"%j), eval("b%dy"%j), eval("b%dw"%j), eval("b%dh"%j))
# Pads
for i in range(8):
	f.add_pad("%d"%(i+1),px,py,pw,ph)
	px += ppitch

f.silk_line(-0.5*ow+ox, -0.5*oh+oy, -0.5*ow+ox, 0.5*oh+oy)
f.silk_line(0.5*ow+ox, -0.5*oh+oy, 0.5*ow+ox, 0.5*oh+oy)
f.silk_line(-0.5*ow+ox, 0.5*oh+oy, 0.5*ow+ox, 0.5*oh+oy)
f.silk_line(-0.5*ow+ox, -0.5*oh+oy, 0.5*ow+ox, -0.5*oh+oy)
f.finish()
