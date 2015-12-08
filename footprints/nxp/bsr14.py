#!/usr/bin/python
import footgen

f = footgen.Footgen("BSR14","geda")

f.add_pad("3", - 0.95,  -1, 0.6, 0.7)
f.add_pad("2",   0.95, -1, 0.6, 0.7)
f.add_pad("1", 0,  1, 0.6, 0.7)


f.silkbox(3.3,1)



f.finish()