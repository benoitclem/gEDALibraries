#!/usr/bin/python
# -*- coding: utf-8 -*-
import footgen

# A => 1
# B,C => 2

y = 0
x = 7.25

w = 14.5
h = 9.0

pADrill = 3.5
pBCDrill = 3
pABCTick = 1

pAx = 13.9
pAy = 0

pBx = 10.7
pBy = -4.7

pCx = 7.7
pCy = 0

clr0 = 0.5
clr1 = 0.1

f = footgen.Footgen("dcplug_trav","geda")
f.add_pin("2", pAx-x, pAy, pADrill, pADrill+pABCTick)
f.add_pin("1", pBx-x, pBy, pBCDrill, pBCDrill+pABCTick)
f.add_pin("1", pCx-x, pCy, pBCDrill, pBCDrill+pABCTick)

# left
f.generator.silk_line(-0.5*w, -0.5*h, -0.5*w, 0.5*h)
# bottom
f.generator.silk_line(-0.5*w, 0.5*h, 0.5*w, 0.5*h)
# top left
f.generator.silk_line(-0.5*w, -0.5*h, pBx-x-(pBCDrill/2)-pABCTick-clr0, -0.5*h)
# top right
f.generator.silk_line(pBx-x+(pBCDrill/2)+pABCTick+clr0, -0.5*h,0.5*w, -0.5*h)
# right bottom
f.generator.silk_line(0.5*w, -0.5*h, 0.5*w, pAy-(pADrill/2)-pABCTick-clr1)
# right left
f.generator.silk_line(0.5*w, 0.5*h, 0.5*w, pAy+(pADrill/2)+pABCTick+clr1)

f.finish()
