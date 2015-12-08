#!/usr/bin/python
import footgen

L = 21.97
H = 5.08
W = 2.79
p = 0.5
p2 = 4

f = footgen.Footgen("BK-912-CR2032","geda")
f.add_pad('1', -L/2, 0, W, H)
f.add_pad('1',  L/2, 0, W, H)

f.generator.options_list = ["circle"]
f.add_pad('2',  0, 0, 17.78, 17.78)
f.generator.options_list = []

f.silk_line(-L/2-W/2-p,-H/2-p,-L/2+W/2,-H/2-p)
f.silk_line(-L/2-W/2-p,-H/2-p,-L/2-W/2-p,+H/2+p)
f.silk_line(-L/2-W/2-p,+H/2+p,-L/2+W/2,+H/2+p)

#f.silk_line(-L/2+W/2,+H/2+p2, -H/2-p2,+L/2-W/2)

f.silk_line(+L/2+W/2+p,-H/2-p,+L/2-W/2,-H/2-p)
f.silk_line(+L/2+W/2+p,-H/2-p,+L/2+W/2+p,+H/2+p)
f.silk_line(+L/2+W/2+p,+H/2+p,+L/2-W/2,+H/2+p)

#f.silk_line(+L/2-W/2,+H/2+p2, +H/2+p2,+L/2-W/2)

f.finish()