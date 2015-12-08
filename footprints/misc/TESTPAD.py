#!/usr/bin/python
import footgen
padSize = 1.0
silkwidth = 0.155
f = footgen.Footgen("TESTPAD1mm","geda")
f.add_pad('1',  0, 0, padSize, padSize)
f.silk_line(-padSize/2+silkwidth,padSize/2+silkwidth,padSize/2-silkwidth,padSize/2+silkwidth)
f.finish()

padSize *= 2

f = footgen.Footgen("TESTPAD2mm","geda")
f.add_pad('1',  0, 0, padSize, padSize)
f.silk_line(-padSize/2+silkwidth,padSize/2+silkwidth,padSize/2-silkwidth,padSize/2+silkwidth)
f.finish()

padSize *= 2

f = footgen.Footgen("TESTPAD4mm","geda")
f.add_pad('1',  0, 0, padSize, padSize)
f.silk_line(-padSize/2+silkwidth,padSize/2+silkwidth,padSize/2-silkwidth,padSize/2+silkwidth)
f.finish()
