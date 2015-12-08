#!/usr/bin/python
import footgen

f = footgen.Footgen("ESP8266-12","geda")
f.pitch = 2
f.pins = 16
f.width = 13
f.padheight = 1.2
f.padwidth = 2.2
f.so()
f.silk_line(-8,8.5, 8, 8.5)
f.silk_line(-8,-8.5, -8, -15.5)
f.silk_line(-8,-15.5, 8, -15.5)
f.silk_line(8, -15.5, 8, -8.5)
f.finish()

