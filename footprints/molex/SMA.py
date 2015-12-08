#!/usr/bin/python
import footgen

gw = 5.08
gh = 2.415
gy = 11.18/2 - gh/2

sw = 5.08
sh = 2.29

f = footgen.Footgen("SMA","geda")
f.add_pad("1",0,0,sw,sh)
f.add_pad("2",0, -gy,gw,gh)
f.add_pad("2",0, gy,gw,gh)
f.generator.options_list = ["bottom"]
f.add_pad("2",0, -gy,gw,gh)
f.add_pad("2",0, gy,gw,gh)
f.finish()
