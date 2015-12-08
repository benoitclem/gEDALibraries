#!/usr/bin/python
import footgen

pw = 1.0
ph = 0.5
off = 0.2
pitch = 2.25

f = footgen.Footgen("SOD323_BAT60","geda")
f.add_pad("2",-pitch/2,0,pw,ph) # K
f.silk_line(-pitch/2+pw/2+off, -ph/2-off, -pitch/2+pw/2+off, +ph/2+off)
f.silk_line(-pitch/2+pw/2+off, 0, +pitch/2-pw/2-off, +ph/2+off)
f.silk_line(-pitch/2+pw/2+off, 0, +pitch/2-pw/2-off, -ph/2-off)
f.add_pad("1",+pitch/2,0,pw,ph)
f.finish()
