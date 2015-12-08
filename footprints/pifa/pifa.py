#!/usr/bin/python
import footgen

L1 = 3.94
L2 = 2.70
L3 = 5.00
L4 = 2.64
L5 = 2.00
L6 = 4.90

W1 = 0.90
W2 = 0.50

D1 = 0.50
D2 = 0.30
D3 = 0.30
D4 = 0.50
D5 = 1.40
D6 = 1.70

sigName = '1'
gndName = '2'

f = footgen.Footgen("PIFA","geda")
#.add_pad(sigName, x, y, xs, ys)
f.add_pad(sigName, 0, 0, W1, L6) 																	# 1
f.add_pad(sigName, D5+W1/2+W2/2, 0, W2, L6) 											# 2
f.add_pad(sigName, L3/2-W1/2, -(L6/2+W2/2), L3, W2) 							# 3
f.add_pad(sigName, L3-W1/2-W2/2, -(L6/2-L4/2), W2, L4) 						# 4
f.add_pad(sigName, L3-W1/2+L5/2, -(L6/2-L4+W2/2), L5, W2) 				# 5
f.add_pad(sigName, L3-W1/2+L5+W2/2, -(L6/2-L4/2), W2, L4) 				# 6
f.add_pad(sigName, L3-W1/2+L5+L2/2, -(L6/2+W2/2), L2, W2) 				# 7
f.add_pad(sigName, L3-W1/2+L5+L2-W2/2, -(L6/2-L4/2), W2, L4)  		# 8
f.add_pad(sigName, L3-W1/2+L5+L2+L5/2, -(L6/2-L4+W2/2), L5, W2)  	# 9
f.add_pad(sigName, L3-W1/2+2*L5+L2+W2/2, -(L6/2-L4/2), W2, L4) 		# 10
f.add_pad(sigName, L3-W1/2+2*L5+L2+L2/2, -(L6/2+W2/2), L2, W2) 		# 11
f.add_pad(sigName, L3-W1/2+2*L5+2*L2-W2/2, -(L6/2-L1/2), W2, L1) 	# 12
f.add_via(gndName, 0, L6/2-D4/2, 0.33, 0.503)											# VIA TO GND
#.silk_line(x1,y1,x2,y2)
f.silk_line(-W1/2-D1,L6/2-D4,-W1/2-D1,-(L6/2+W2+D2))													# LEFT
f.silk_line(-W1/2-D1,-(L6/2+W2+D2),L3-W1/2+2*L5+2*L2+D3,-(L6/2+W2+D2)) 				# UP
f.silk_line(L3-W1/2+2*L5+2*L2+D3,-(L6/2+W2+D2),L3-W1/2+2*L5+2*L2+D3,L6/2-D4) 	# RIGHT
f.silk_line(L3-W1/2+2*L5+2*L2+D3,L6/2-D4,-W1/2-D1,L6/2-D4) 										# DOWN
f.finish()