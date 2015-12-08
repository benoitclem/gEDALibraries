#!/usr/bin/python
import footgen

f = footgen.Footgen("QFN40_DA14580","geda")
f.pitch = 0.4
f.pins = 40
f.width = 4.1
f.padheight = 0.25
f.padwidth = .8
f.qfn()
f.thermal_pad(3.7)
f.via_array(columns=3, rows=3, pitch=1)
f.silk_crop(5.1, pin1="circle")
f.finish()
