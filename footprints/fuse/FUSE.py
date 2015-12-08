#!/usr/bin/python
import footgen

pw = 1.96
ph = 3.16
off = 0.2
pitch = 6.86 - 1.96

f = footgen.Footgen("2PADFUSE","geda")
f.add_pad("2",-pitch/2,0,pw,ph)
f.add_pad("1",+pitch/2,0,pw,ph)
f.silk_line(0, -ph/2-off, 0, +ph/2+off)
f.finish()
