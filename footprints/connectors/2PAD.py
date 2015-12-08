#!/usr/bin/python
import footgen

pw = 2.0
ph = 2.0
pPitch = 1.0 + pw
off = 0.3

f = footgen.Footgen("2PAD","geda")
f.add_pad("1",-pPitch/2,0,pw,ph)
f.add_pad("2",+pPitch/2,0,pw,ph)
f.silkbox(pPitch+pw+off,ph+off)
f.finish()
