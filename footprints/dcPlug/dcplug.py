#!/usr/bin/python
import footgen

pABDrill = 3
pABCTick = 0.1
pAx = 13.9
pAy = 0

pBx = 10.7
pBy = 4.7

pCDrill = 3.5
pCx = 7.7
pCy = 0

f = footgen.Footgen("dcplug_smt","geda")
f.add_pin("0", pAx, pAy, pABDrill, pABDrill+pABCTick)
f.add_pin("0", pBx, pBy, pABDrill, pABDrill+pABCTick)
f.add_pin("0", pCx, pCy, pABDrill, pCDrill+pABCTick)
f.finish()
