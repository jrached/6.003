#!/usr/bin/env python3
from lib6003.audio import wav_read, wav_write
from math import pi, sin, cos, e
from matplotlib.pyplot import stem, show, plot

tune = [
    (369.99, 0.16666666666666666), (415.3, 0.16666666666666666),
    (440.0, 0.5), (369.99, 0.5), (369.99, 0.3333333333333333),
    (369.99, 0.16666666666666666), (369.99, 0.3333333333333333),
    (369.99, 0.3333333333333333), (329.63, 0.16666666666666666),
    (369.99, 0.3333333333333333), (369.99, 0.3333333333333333),
    (329.63, 0.16666666666666666), (329.63, 0.5),
    (246.94, 0.3333333333333333), (493.88, 0.3333333333333333),
    (246.94, 0.3333333333333333), (493.88, 0.3333333333333333),
    (369.99, 0.16666666666666666), (415.3, 0.16666666666666666),
    (440.0, 0.5), (369.99, 0.5), (369.99, 0.3333333333333333),
    (369.99, 0.16666666666666666), (369.99, 0.3333333333333333),
    (369.99, 0.3333333333333333), (329.63, 0.16666666666666666),
    (369.99, 0.3333333333333333), (369.99, 0.3333333333333333),
    (329.63, 0.16666666666666666), (329.63, 0.5),
    (246.94, 0.3333333333333333), (493.88, 0.3333333333333333),
    (246.94, 0.3333333333333333), (493.88, 0.6666666666666666),
    (277.18, 0.3333333333333333), (369.99, 0.3333333333333333),
    (415.3, 0.3333333333333333), (440.0, 0.3333333333333333),
    (415.3, 0.16666666666666666), (440.0, 0.16666666666666666),
    (415.3, 0.16666666666666666), (369.99, 0.16666666666666666),
    (415.3, 0.3333333333333333), (369.99, 0.3333333333333333),
    (277.18, 1.3333333333333333), (246.94, 1.1666666666666665),
    (277.18, 0.16666666666666666), (277.18, 0.3333333333333333),
    (369.99, 0.3333333333333333), (415.3, 0.3333333333333333),
    (440.0, 0.3333333333333333), (415.3, 0.6666666666666666),
    (369.99, 0.6666666666666666), (277.18, 1.3333333333333333),
    (246.94, 1.3333333333333333), (277.18, 0.3333333333333333),
    (369.99, 0.3333333333333333), (415.3, 0.3333333333333333),
    (440.0, 0.3333333333333333), (415.3, 0.16666666666666666),
    (440.0, 0.16666666666666666), (415.3, 0.16666666666666666),
    (369.99, 0.16666666666666666), (415.3, 0.3333333333333333),
    (369.99, 0.3333333333333333), (277.18, 1.3333333333333333),
    (246.94, 1.1666666666666665), (277.18, 0.16666666666666666),
    (277.18, 0.3333333333333333), (369.99, 0.3333333333333333),
    (415.3, 0.3333333333333333), (440.0, 0.3333333333333333),
    (415.3, 0.6666666666666666), (369.99, 0.6666666666666666),
    (277.18, 1.3333333333333333), (246.94, 1.3333333333333333),
    (277.18, 1.3333333333333333)]

# generate the template from "oboe_C4.wav"
oboe_note, oboe_sampling_rate = wav_read("oboe_C4.wav")
sax_note, sax_sampling_rate = wav_read("sax_C4.wav")
trumpet_note, trumpet_sampling_rate = wav_read("trumpet_C4.wav")
fs = 44100

def old_synthesis(omega_t):
	return 0.5*sin(omega_t) + 0.2*cos(2*omega_t) + 0.3*cos(4*omega_t - pi/4)

def synthesis(a_k, n, k, upper_n):
	omega = 2*pi/upper_n
	return a_k*e**(1j*k*omega*n)

def analysis(f, n, k, upper_n):
	omega = 2*pi/upper_n
	return f*e**(-1j*k*omega*n)
	
def get_coefficients(note, sampling_rate):
	upper_n = sampling_rate/261
	coeffs = []
	
	for k in range(0, int(upper_n)): 
		n = 0
		sum_ = 0 + 0j
		for pulse in note[20000: 20000 + int(upper_n)]:
			sum_ += analysis(pulse, n, k, upper_n)
			n += 1
		coeff = sum_/upper_n
		coeffs.append(coeff)
	
	return coeffs
	
def reconstruct_song(coeffs):
	song = []
	n = 0
	
	for frequency, duration in tune:
		num_samples = round(fs*duration)
		for _ in range(num_samples):
			k = 0
			sum_ = 0 + 0j
			
			for a_k in coeffs:
				upper_n = fs/frequency
				sum_ += synthesis(a_k, n, k, upper_n)
				k += 1
			n += 1
			song.append(sum_)
	return song
	
	
oboe_coeffs = get_coefficients(oboe_note, oboe_sampling_rate)
oboe_song = reconstruct_song(oboe_coeffs)
wav_write(oboe_song, fs, 'oboe_song.wav')

trumpet_coeffs = get_coefficients(trumpet_note, trumpet_sampling_rate)
trumpet_song = reconstruct_song(trumpet_coeffs)
wav_write(trumpet_song, fs, 'trumpet_song.wav')

sax_coeffs = get_coefficients(sax_note, sax_sampling_rate)
sax_song = reconstruct_song(sax_coeffs)
wav_write(sax_song, fs, 'sax_song.wav')


