#!/usr/bin/python
import footgen

f = footgen.Footgen("ZX62-B-5PA","geda")
f.padwidth = 1.35
f.padheight = 0.4
f.pitch = 0.65
f.rowofpads((0,-2.675),"right",1,5)

f.add_pad("6",-3.1,-2.55,2.1,1.6)
f.add_pad("6",3.1,-2.55,2.1,1.6)

f.add_pad("6",-4.05,0,1.9,1.9)
f.add_pad("6",-1.2,0,1.9,1.9)
f.add_pad("6",1.2,0,1.9,1.9)
f.add_pad("6",4.05,0,1.9,1.9)

f.silk_line(-4.9,  1.45, 4.9, 1.45)

f.finish()