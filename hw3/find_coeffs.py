#!/usr/bin/env python3

from math import pi, e
from matplotlib.pyplot import stem, show

#f, upper_n = question5()

def find_coeffs(function, upper_n, mag=False):
	coeffs = []
	for k in range(upper_n):
		sum_ = 0 + 0j
		for n in range(upper_n):
			sum_ += f[n]*e**(-1j*k*n*2*pi/upper_n)
		if not mag:
			coeffs.append(sum_/upper_n)
		else:
			coeffs.append(abs(sum_/upper_n))

	return coeffs
	
def plot_coeffs(coefficients, upper_n):
	ks = [k for k in range(upper_n)]
	stem(ks, coefficients)
	show()
	
coeffs = find_coeffs(f, upper_n)
print(coeffs)
#plot_coeffs(coeffs, upper_n)


def question5():
	upper_n = 51

	f = []
	for i in range(51):
		f.append(0)
		
	for i in list(range(5,11)):
		f[i] = 0.5

	for i in list(range(11,13)):
		f[i] = 0.8
		
	add = 0
	for i in list(range(13, 18)):
		f[i] = 0.9 + add
		add += 0.02
		
	sub = 0
	for i in list(range(18, 23)): 
		f[i] = 9.98 - sub
		sub += 0.02
		
	for i in list(range(23,25)):
		f[i] = 0.8
		
	for i in list(range(25,31)):
		f[i] = 0.5
	return f, upper_n
