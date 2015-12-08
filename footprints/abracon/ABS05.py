#!/usr/bin/python
import footgen

silkwidth = 0.2

f = footgen.Footgen("ABS05","geda")
f.width = 0.6
f.padheight = 1
f.padwidth = 0.5
f.twopad()
f.finish()