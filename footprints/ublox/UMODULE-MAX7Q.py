#!/usr/bin/python
import footgen

f = footgen.Footgen("UMODULE-MAX7Q","geda")
f.pitch = 1.1
f.pins = 18
f.width = 7.7
f.padheight = 0.8
f.padwidth = 2	# Here the soft does not have capability of multiple pad width
f.soc(0.2)
f.silk_crop(9.7,10.1)
f.finish()