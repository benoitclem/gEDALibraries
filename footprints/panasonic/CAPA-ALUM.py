#!/usr/bin/python
import footgen



def CAPA_ALUM(t,pw,ph,pitch,off, ow,oh,clr,obev):
	f = footgen.Footgen("CAPA_ALUM_"+t,"geda")
	f.add_pad("2",0,-pitch/2,pw,ph) # negative pad
	f.add_pad("1",0,+pitch/2,pw,ph) # positive pad (bevel side)
	f.silk_line(-pw/2-clr,-oh/2,-ow/2,-oh/2)
	f.silk_line(-ow/2,-oh/2,-ow/2,+oh/2-obev)
	f.silk_line(-ow/2,+oh/2-obev,-ow/2+obev,+oh/2)
	f.silk_line(-ow/2+obev,+oh/2,-pw/2-clr,+oh/2)
	f.silk_line(+pw/2+clr,-oh/2,+ow/2,-oh/2)
	f.silk_line(+ow/2,-oh/2,+ow/2,+oh/2-obev)
	f.silk_line(+ow/2,+oh/2-obev,+ow/2-obev,+oh/2)
	f.silk_line(+ow/2-obev,+oh/2,+pw/2+clr,+oh/2)
	f.finish()

pw = 1.5
ph = 4
off = 0.2
pitch = 3.1+ph

ow = 8.3
oh = 8.3
clr = 0.2
obev = 1.3

CAPA_ALUM("F",pw,ph,pitch,off, ow,oh,clr,obev)

pw = 0.8
ph = 2.0
off = 0.2
pitch = 1.0+ph

ow = 4.3
oh = 4.3
clr = 0.2
obev = 0.7

CAPA_ALUM("B",pw,ph,pitch,off, ow,oh,clr,obev)
