#!/usr/bin/python
import footgen

h = 16.55

# thermal pad
tpw = 10.49
tph = 8.38
# pads
pw = 1.016
ph = 3.504
pitch = 5.08
px = pitch/2
py = h-tph/2-ph/2
# outline$
clr = 1
ow = tpw + clr*2 
oh = h + clr*2
ox = 0
oy = 3.8875


f = footgen.Footgen("MC7800-D2PAK-3","geda")
# Thermal pad
f.add_pad("2",0,0,tpw,tph)
# OUT
f.add_pad("3",px,py,pw,ph)
# IN
f.add_pad("1",-px,py,pw,ph)
# OUTLINE
f.silk_line(-0.5*ow+ox, -0.5*oh+oy, -0.5*ow+ox, 0.5*oh+oy)
f.silk_line(0.5*ow+ox, -0.5*oh+oy, 0.5*ow+ox, 0.5*oh+oy)
f.silk_line(-0.5*ow+ox, 0.5*oh+oy, 0.5*ow+ox, 0.5*oh+oy)
f.silk_line(-0.5*ow+ox, -0.5*oh+oy, 0.5*ow+ox, -0.5*oh+oy)
f.finish()
