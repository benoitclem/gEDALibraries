#!/usr/bin/python
import footgen

n = 4.0
drill = 0.55
thick = 0.55
thickOneSide = thick/2
pitch = 2.54
x = -((n-1.0)*pitch)/2
y = -4.5/2
clr = 0.2

pcbThick = 1.0
ow = pitch * n
ohA = 4.5 + drill/2 + thickOneSide + clr
ohB = pitch + pcbThick
ohyA = -(drill/2 + thickOneSide + clr)/2
ohyB = -pcbThick/2

pinClr = 1
pinLen = 3

# NO PASTE IS NOT WORKING / NO TIME TO RESOLVE / DONE IN FP FILE DIRECTLY
1/0

def silkbox(f,x,y,w,h):
	# left
	f.silk_line(-0.5*w+x, -0.5*h+y, -0.5*w+x, 0.5*h+y)
	# right
	f.silk_line(0.5*w+x, -0.5*h+y, 0.5*w+x, 0.5*h+y)
	# bottom
	f.silk_line(-0.5*w+x, 0.5*h+y, 0.5*w+x, 0.5*h+y)
	# top
	f.silk_line(-0.5*w+x, -0.5*h+y, 0.5*w+x, -0.5*h+y)

f = footgen.Footgen("PIN_CONN_ANGLE_A","geda")
f.options_list.append("nopaste")
for i in range(int(n)):
	f.add_pin("%d"%(i+1),x,y,drill,drill+thick)
	f.silk_line(x, y+pinClr, x, y+pinClr+pinLen)				# TOP
	x += pitch
silkbox(f,0,ohyA,ow,ohA)
f.finish()

x = -((n-1.0)*pitch)/2
y = 0

f = footgen.Footgen("PIN_CONN_ANGLE_B","geda")
f.options_list.append("nopaste")
for i in range(int(n)):
	f.add_pin("%d"%(i+1),x,y,drill,drill+thick)					# BOX
	x += pitch
f.silk_line(-0.5*ow,-0.5*pitch, 0.5*ow,-0.5*pitch)	
silkbox(f,0,ohyB,ow,ohB)
f.finish()
