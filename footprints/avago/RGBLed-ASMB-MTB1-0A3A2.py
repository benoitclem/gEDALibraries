#!/usr/bin/python
import footgen

padwidth = 1.1
padheight = 1.5
deltax = 0.4/2 + padwidth/2
deltay = 1.5/2 + padheight/2

f = footgen.Footgen("RGBLed-ASMB-MTB1-0A3A2","geda")
print(deltax,deltay)
f.add_pad("1", - deltax,  deltay, padwidth, padheight)
f.add_pad("2", - deltax, -deltay, padwidth, padheight)
f.add_pad("3",   deltax, -deltay, padwidth, padheight)
f.add_pad("4",   deltax,  deltay, padwidth, padheight)
f.finish()