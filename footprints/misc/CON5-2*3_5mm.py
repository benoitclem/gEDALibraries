#!/usr/bin/python
import footgen

f = footgen.Footgen("CON5-2*1_6mm","geda")
f.padwidth = 2
f.padheight = 1.6
f.pitch = 2.2
f.rowofpads((0,-2.675),"down",1,5)


f.finish()