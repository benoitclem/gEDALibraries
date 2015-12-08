#!/usr/bin/python
import footgen

pw = 1.52
ph = 1.68
off = 0.5
pitch = 5.58-pw

f = footgen.Footgen("DO-214B","geda")
f.add_pad("2",-pitch/2,0,pw,ph)
f.silk_line(-pitch/2+pw/2+off, -ph/2-off, -pitch/2+pw/2+off, +ph/2+off)
f.silk_line(-pitch/2+pw/2+off, 0, +pitch/2-pw/2-off, +ph/2+off)
f.silk_line(-pitch/2+pw/2+off, 0, +pitch/2-pw/2-off, -ph/2-off)
f.add_pad("1",+pitch/2,0,pw,ph)
f.finish()
