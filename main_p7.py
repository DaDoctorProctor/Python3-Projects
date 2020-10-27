from numpy import cos, sin, pi, arange, zeros, array, linspace, round
import plotly.graph_objects as go
from palitos2 import stem_plot
from mi_dft_func import mi_dft_func
from mi_idft_func import mi_idft_func
import matplotlib.pyplot as plt
import gc
gc.collect()

file = open("coeff_real.txt", "r")
lines = file.readlines()
file.close()

real = []
for line in lines:
	real.append(float(line))
n = arange(0, len(real))

plt.figure()
plt.title("Real Coeficients") 
plt.stem(n,real)
plt.xlabel('Number of Samples')
plt.ylabel('Real values')
plt.xlim(n[0],n[-1])
plt.title("0. Real coefficients X(m)")
plt.legend()

#---------------------------------------
file = open("coeff_imag.txt", "r")
lines = file.readlines()
file.close()

imag = []
for line in lines:
	imag.append(float(line))
n = arange(0, len(imag))

plt.figure()
plt.stem(n,imag)
plt.xlabel('Number of Samples')
plt.ylabel('Imaginary values')
plt.xlim(n[0],n[-1])
plt.title("0. Imaginary coefficients X(m)")
plt.legend()

#Join both coefficients to make a single X(m)!
Xm = array(real) + array(imag)*1j

realIDFT, imagIDFT = mi_idft_func(Xm)

#Applying the IDFT, we are back to the X(N) domain!

#Real IDFT
plt.figure()
plt.stem(n,realIDFT)
plt.xlabel('Number of Samples')
plt.ylabel('Real coefficients')
plt.xlim(n[0],n[-1])
plt.title("1. Real coefficients, X(m)")
plt.legend()

#Imaginary IDFT
plt.figure()
plt.stem(n,imagIDFT)
plt.xlabel('Number of Samples')
plt.ylabel("Imaginary coefficients")
plt.xlim(n[0],n[-1])
plt.title("1. Imaginary coefficients, X(m)")
plt.legend()

xn = realIDFT
xn1 = imagIDFT

fs = 70
ts = 1/fs
xfs = n*ts

#After time transformation Real
plt.figure()
plt.plot(xfs,realIDFT)
plt.xlabel('Time (S)')
plt.ylabel('Real')
plt.xlim(xfs[0],xfs[-1])
plt.title("2. Real coefficients X(n)")
plt.legend()

#After time transformation Imag
plt.figure()
plt.plot(xfs,imagIDFT)
plt.xlabel('Time (S)')
plt.ylabel('Imaginary')
plt.xlim(xfs[0],xfs[-1])
plt.title("2. Imaginary coefficients X(n)")
plt.legend()

import scipy.fft
s = scipy.fft.ifft(Xm)
print(s)

#Using Scipy IFFT
plt.figure()
plt.plot(xfs,s)
plt.xlabel('Time (S)')
plt.ylabel('Values.')
plt.xlim(xfs[0],xfs[-1])
plt.title("Ex. Using IFFT by Scipy, X(n)")
plt.legend()

plt.show()

