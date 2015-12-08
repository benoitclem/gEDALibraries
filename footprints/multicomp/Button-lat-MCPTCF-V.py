#!/usr/bin/python
import footgen

padwidth = 1.45
padheight = 1.0
deltax = 3.7/2 + padwidth/2
deltay = 0.7/2 + padheight/2

f = footgen.Footgen("Button-Lat-MCPTCF","geda")
print(deltax,deltay)

f.add_pad("2", - deltax,  deltay, padwidth, padheight)
f.add_pad("1", - deltax, -deltay, padwidth, padheight)
f.add_pad("3",   deltax, -deltay, padwidth, padheight)
f.add_pad("4",   deltax,  deltay, padwidth, padheight)
f.add_pin("",0,-1.35,0.75,0.8)
f.add_pin("",0,1.35,0.75,0.8)

f.silk_line(-1.1, 0, -1.1, 0.3)
f.silk_line(-1.1, 0.3, 1.1, 0.3)
f.silk_line(1.1, 0.3, 1.1, 0)

f.silk_line(-2.35, -1.9, 2.35, -1.9)
f.silk_line(-2.35,  1.9, 2.35, 1.9)

f.finish()