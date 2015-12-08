#!/usr/bin/python
import footgen

f = footgen.Footgen("LGA16_L3GD20H","geda")
f.pitch = 0.5
f.pins = 16
f.height = 1.9
f.width = 1.9
f.padheight = 0.35
f.padwidth = .45	# Here the soft does not have capability of multiple pad width
f.pinshigh = 5
f.pinswide = 3
f.sm_pads()
f.silk_crop(3.1,3.1, pin1="circle")
f.finish()
