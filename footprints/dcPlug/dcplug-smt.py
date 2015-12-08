#!/usr/bin/python
import footgen

gph = 3.9
gpw = 6.2
gpy = 4.5+gph/2

sph = 3.3
spw = 4.4
spy = 0
spx = 9

hx = -3.8
hs = 2

oh = 9.0
ow = 13.6
clr = 0.5

f = footgen.Footgen("dcplug-smt","geda")
f.add_pad("1", 0, -gpy, gpw, gph) 																							# 1
f.add_pad("1", 0, +gpy, gpw, gph) 																							# 1
f.add_pad("2", spx, spy, spw, sph) 																							# 2
# Metallisation ???
f.add_via(pin = "3", x = hx, y = 0, size = hs+1, pad = hs)											# 3 hole 
f.silk_line(-ow/2,-oh/2,-gpw/2-clr,-oh/2)
f.silk_line(-ow/2,-oh/2,-ow/2,oh/2)
f.silk_line(-ow/2,+oh/2,-gpw/2-clr,+oh/2)
f.silk_line(gpw/2+clr,-oh/2,ow/2,-oh/2)
f.silk_line(ow/2,-oh/2,ow/2,-sph/2-clr+spy)
f.silk_line(ow/2,sph/2+clr+spy,ow/2,oh/2)
f.silk_line(gpw/2+clr,oh/2,ow/2,oh/2)
f.finish()
