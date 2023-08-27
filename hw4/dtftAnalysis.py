#!/usr/bin/env python3

import sys
from math import pi, e
from matplotlib.pyplot import plot, show

omega = -pi
big_x = []
omegas = []

alpha = float(sys.argv[1])
m = int(sys.argv[2])
eps = 0.01
inf = 100

def delta(arg):
	if arg < eps:
		return 1
	else:
		return 0
	
while omega <= pi:
	sum_1 = 0
	for n in range(-inf, inf):
		x_n = 0
		for i in range(-inf, inf):
			x_n += (alpha**i)*delta(n - i*m) 		
		sum_1 += x_n*e**(-1j*omega*n)
	big_x.append(abs(sum_1))
	omegas.append(omega)
	omega += pi/10

print("alpha: {}, m: {}".format(alpha, m))	
plot(omegas, big_x)
show()
