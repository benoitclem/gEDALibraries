#!/usr/bin/python
import footgen

f = footgen.Footgen("LGA16_ADXL362","geda")
f.pitch = 0.5
f.pins = 16
f.height = 1.75
f.width = 1.9
f.padheight = 0.3
f.padwidth = .85	# Here the soft does not have capability of multiple pad width
f.pinshigh = 5
f.pinswide = 3
f.sm_pads()
f.silk_crop(3.25,3, pin1="circle")
f.finish()
