#!/usr/bin/python
import footgen

padSize = 1.0
silkwidth=0.155
f = footgen.Footgen("CON10-1_27mm","geda")
f.diameter = 0.9
f.width = 1.27
f.pins = 10
f.drill = 0.5
f.pitch = 1.27
f.dip()
f.finish()