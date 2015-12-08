#!/usr/bin/python
import footgen

h = 16.55

# thermal pad
tpw = 3.25
tph = 2.15
tpx = 0
tpy = -2.9
# pads
pw = 0.95
ph = 2.15
pitch = 2.3
px = pitch
py = 2.9
# outline$
ow = 6.7
oh = 3.7
clr = 0.5

f = footgen.Footgen("AP1117-SOT223","geda")
# Thermal pad (OUT)
f.add_pad("2",tpx,tpy,tpw,tph)
# GND
f.add_pad("1",-px,py,pw,ph) # 
# OUT
f.add_pad("2",0,py,pw,ph) #
# IN
f.add_pad("3",px,py,pw,ph) #
# OUTLINE
f.silkbox(ow-clr,oh-clr)
f.finish()
