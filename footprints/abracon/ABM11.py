#!/usr/bin/python
import footgen

silkwidth = 0.2

f = footgen.Footgen("ABM11","geda")
f.pitch = 1
f.pins = 4
f.height = 1.6
f.width = 0.55
f.realWidth = 2.0
f.padheight = 0.65
f.padwidth = 0.75
f.so()
f.silkbox(2+silkwidth,1.6+silkwidth)
f.finish()

print("/!\/!\/!\ For this foot print you have to set the correct pin name into fp file")
print("(1) -> 4(GND) / (2) -> 1(SIG1) / (3) -> 2(GND) / (4) -> 3(SIG2)")