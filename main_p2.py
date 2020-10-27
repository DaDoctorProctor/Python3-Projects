from numpy import cos, sin, pi, arange, zeros, array, linspace, round, ones, arctan2, sqrt
import plotly.graph_objects as go
from mi_dft_func import mi_dft_func
from mi_idft_func import mi_idft_func
import matplotlib.pyplot as plt

import gc
gc.collect()

#Inicial data
n = arange(0,10)
fs = 70  #Sampling at 70 Hz!
ts = 1/fs

t = linspace(0,10,70)

x1t = 3*cos(2*pi*(1/7)*t) 
x2t = 0.8*sin(2*pi*(2/5)*t)
x3t = x1t + x2t

plt.figure()
plt.plot(t, x1t)
plt.xlabel('Time (S)')
plt.ylabel('Xs(m)')
plt.xlim(t[0],t[-1])
plt.title("0. X1s(m)")
plt.legend()

plt.figure()
plt.plot(t, x2t)
plt.xlabel('Time (S)')
plt.ylabel('Xs(m)')
plt.xlim(t[0],t[-1])
plt.title("0. X2s(m)")
plt.legend()

plt.figure()
plt.plot(t, x3t)
plt.xlabel('Time (S)')
plt.ylabel('Xs(m)')
plt.xlim(t[0],t[-1])
plt.title("0. X1s(m) + X2s(m)")
plt.legend()


#To be sampled at 70 Hz ts must be multiplied.
x1n = 3*cos(2*pi*(1/7)*n*ts) 
x2n = 0.8*sin(2*pi*(2/5)*n*ts)
x3n = x1n + x2n

N = len(x1n)
AF = fs/N
AFn = AF*n

x1n_real,x1n_imag,x1n_mags,x1n_angs = mi_dft_func(x1n)
x2n_real,x2n_imag,x2n_mags,x2n_angs = mi_dft_func(x2n)

xSn_real,xSn_imag,xSn_mags,xSn_angs = mi_dft_func(x3n)

XM_real = x1n_real + x2n_real
XM_imag = x1n_imag + x2n_imag

#3. Plot the magnitude and angle of X's(m) = Xm1 + Xm2
XM_mags = sqrt(XM_real**2 + XM_imag**2)
XM_angs = arctan2(XM_real, XM_imag)

plt.figure()
plt.stem(AFn, XM_mags)
plt.xlabel('Hertz (Hz)')
plt.ylabel('Magnitudes')
plt.xlim(AFn[0],AFn[-1])
plt.title("3. X's(m) Magnitudes")
plt.legend()

plt.figure()
plt.stem(AFn, XM_angs)
plt.xlabel('Hertz (Hz)')
plt.ylabel('Angles')
plt.xlim(AFn[0],AFn[-1])
plt.title("3. X's(m) Angles")
plt.legend()

#2. Plot the magnitude and angle Xs(m)
XMS_mags = sqrt(xSn_real**2+xSn_imag**2)
XMS_angs = arctan2(xSn_real, xSn_imag)

plt.figure()
plt.stem(AFn, XMS_mags)
plt.xlabel('Hertz (Hz)')
plt.ylabel('Magnitudes')
plt.xlim(AFn[0],AFn[-1])
plt.title("2. Xs(m) Magnitudes")
plt.legend()

plt.figure()
plt.stem(AFn, XMS_angs)
plt.xlabel('Hertz (Hz)')
plt.ylabel('Angles')
plt.xlim(AFn[0],AFn[-1])
plt.title("2. Xs(m) Angles")
plt.legend()

#4. Plot final difference between XM_Final minus XMA_Final
XM_Final = XMS_mags - XM_mags
XMA_Final = XMS_angs - XM_angs

plt.figure()
plt.stem(AFn, XM_Final)
plt.xlabel('Hertz (Hz)')
plt.ylabel('Magnitudes')
plt.xlim(AFn[0],AFn[-1])
plt.title("4. Xs(m) - X's(m) Magnitudes")
plt.legend()

plt.figure()
plt.stem(AFn, XMA_Final)
plt.xlabel('Hertz (Hz)')
plt.ylabel('Angles')
plt.xlim(AFn[0],AFn[-1])
plt.legend()
plt.title("4. Xs(m) - X's(m) Angles")

plt.show()