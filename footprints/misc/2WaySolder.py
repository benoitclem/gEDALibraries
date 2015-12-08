#!/usr/bin/python
import footgen
padSize = 1.3
f = footgen.Footgen("2WaySolder","geda")
f.add_pad('2',  -1.7, 0, padSize, padSize)
f.add_pad('1',  0, 0, padSize, padSize)
f.add_pad('3',  1.7, 0, padSize, padSize)
f.finish()