#!/usr/bin/python
import footgen

f = footgen.Footgen("SCREEN096-1","geda")
f.pitch = 0.7
f.padheight = 0.4
f.padwidth = 2.2
f.rowofpads((0, 0), "up", 1, 30)
f.finish()
