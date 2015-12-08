#!/usr/bin/python
import footgen

cNumber = 4

f = footgen.Footgen("MOLEX_RJ45_TRAV","geda")

w = 15.75
h = 14.99
y = -2.42

bDrill = 3.25
bTic = 0
bX = 12.7 /2

cDrill = 0.89
cTic = 0.7
cPitch = 1.02 
cX0 = 3.81
cX1 = 2.79
cY0 = -2.54 
cY1 = -4.32

m = 1
n = 2
for i in range(cNumber):
	f.add_pin("%d"%m, cX0, cY0, cDrill, cDrill+cTic)
	f.add_pin("%d"%n, cX1, cY1, cDrill, cDrill+cTic)
	m += 2
	n += 2
	cX0 -= cPitch*2
	cX1 -= cPitch*2

f.add_pin("9", -bX, 0, bDrill, bDrill+bTic)
f.add_pin("9", +bX, 0, bDrill, bDrill+bTic)

# left
f.generator.silk_line(-0.5*w, -0.5*h+y, -0.5*w, 0.5*h+y)
# right
f.generator.silk_line(0.5*w, -0.5*h+y, 0.5*w, 0.5*h+y)
# bottom
f.generator.silk_line(-0.5*w, 0.5*h+y, 0.5*w, 0.5*h+y)
# top
f.generator.silk_line(-0.5*w, -0.5*h+y, 0.5*w, -0.5*h+y)

f.finish()
