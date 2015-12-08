#!/usr/bin/python
import footgen

f = footgen.Footgen("SOIC_MCP2551","geda")
f.pitch = 1.27
f.pins = 8
f.width = 3.9
f.padheight = 0.6
f.padwidth = 1.5	# Here the soft does not have capability of multiple pad width
f.so()
f.silkbox(3.4,5.4,1)
f.finish()
