#!/usr/bin/python
import footgen

# Contact Consts
cNumber = 8
cHigh = 6.35
cWidth = 0.76
cPitch = 1.27
cY = -10.325
cX = -((cNumber-1) * cPitch)/2
cXBorder = cX - cWidth/2

# Body Consts
bHigh = 2.8
bWidth = 5.15
bX = 5.5 + bWidth/2

# Outline Consts
oWidth = 15.24
oHigh = 19.2
oY = -1.8
marge = 0.5

f = footgen.Footgen("MOLEX_RJ45_CMS","geda")
# Create Contacts
for i in range(cNumber):
	f.add_pad("%d"%(i+1), cX, cY, cWidth, cHigh)
	cX += cPitch
# Create Body Contact
f.add_pad("9", -bX, 0, bWidth, bHigh)
f.add_pad("9", +bX, 0, bWidth, bHigh)
# Create Outline
f.silk_line(-oWidth/2,-bHigh/2-marge,-oWidth/2,-oHigh/2+oY)											# VERT UPPER LEFT
f.silk_line(-oWidth/2,-oHigh/2+oY,cXBorder-marge,-oHigh/2+oY)										# HOR UPPER LEFT
f.silk_line(oWidth/2,-bHigh/2-marge,oWidth/2,-oHigh/2+oY)												# VERT UPPER RIGHT
f.silk_line(oWidth/2,-oHigh/2+oY,-cXBorder+marge,-oHigh/2+oY)										# HOR UPPER RIGHT								
f.silk_line(-oWidth/2,+bHigh/2+marge,-oWidth/2,oHigh/2+oY)											# VERT LOWER LEFT
f.silk_line(-oWidth/2,oHigh/2+oY,oWidth/2,oHigh/2+oY)												# HOR LOWER
f.silk_line(oWidth/2,+bHigh/2+marge,oWidth/2,oHigh/2+oY)												# VERT LOWER RIGHT

f.finish()

