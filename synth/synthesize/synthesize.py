#!/usr/bin/env python3

from math import sin, cos, pi
from matplotlib.pyplot import plot, show
from lib6003.audio import wav_write

# example plot: f(t) = cos(2*pi*t)
t_list = []          # list of times
f_list = []          # list of corresponding values of f(t)
t = -1
#while t<1:
#   t_list.append(t)
#    f_list.append(cos(2*pi*t))
#    t += 0.01
#plot(t_list,f_list)
#show()

# example wav file: (440 Hz) tone
fs = 44100   # sampling frequency (44.1 kHz)
#fs = 20000
T  = 1/fs    # sampling period
t_list = []          # list of times
f_list = []          # list of corresponding values of f(t)
t = 0

#while t<1:
#    t_list.append(t)
#    f_list.append(0.2*cos(2*pi*440*t))
#    t += T
#wav_write(f_list,fs,'sample.wav')

# fetching c_k and d_k for mystery signal
import pickle
with open('mystery.pkl','rb') as f:
    c_k,d_k = pickle.load(f)
    
t_list = []          # list of times
f_list = []          # list of corresponding values of f(t)
t = 0
m = len(c_k)
omega = 2*pi*15000/fs

while t<2.9:
    t_list.append(t)
    sum_ = 0
    for k in range(m):
    	sum_ += 0*c_k[k]*cos(k*omega*t) + d_k[k]*sin(k*omega*t)
    f_list.append(sum_)
    t += T
wav_write(f_list,fs,'lab2_2c.wav')
plot(t_list, f_list)
show()
