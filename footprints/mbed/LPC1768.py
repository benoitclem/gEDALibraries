#!/usr/bin/python
import footgen

f = footgen.Footgen("LPC1768","geda")
f.pitch = 2.54
f.drill = 0.9
f.diameter = 2
f.pins = 40
f.width = 22.86
f.dip()
f.finish()