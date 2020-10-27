from numpy import cos, sin, pi, arange, zeros, array, linspace, round, ones,max
import plotly.graph_objects as go
from mi_dft_func import mi_dft_func
from mi_idft_func import mi_idft_func
import matplotlib.pyplot as plt

from palitos2 import stem_plot
import gc
gc.collect()

#Inicial data
n = arange(0,100)
fs = 100
ts = 1/fs

#Get XN as output.
#Array for the sum of K.
#for k in arange(1,11):
    #xn = (4/pi)*((sin(2*pi * (2*k - 1) * 2*n*ts))/(2*k-1)) #n*ts

xn = 4/pi*(sin(2*pi*(2*1-1)*2*n*ts)/(2*1-1))
+ 4/pi*(sin(2*pi*(2*2-1)*2*n*ts)/(2*2-1))\
+ 4/pi*(sin(2*pi*(2*3-1)*2*n*ts)/(2*3-1))\
+ 4/pi*(sin(2*pi*(2*4-1)*2*n*ts)/(2*4-1))\
+ 4/pi*(sin(2*pi*(2*5-1)*2*n*ts)/(2*5-1))\
+ 4/pi*(sin(2*pi*(2*6-1)*2*n*ts)/(2*6-1))\
+ 4/pi*(sin(2*pi*(2*7-1)*2*n*ts)/(2*7-1))\
+ 4/pi*(sin(2*pi*(2*8-1)*2*n*ts)/(2*8-1))\
+ 4/pi*(sin(2*pi*(2*9-1)*2*n*ts)/(2*9-1))\
+ 4/pi*(sin(2*pi*(2*10-1)*2*n*ts)/(2*10-1))



plt.figure()
plt.stem(n, xn)
plt.xlabel('Number of Samples')
plt.ylabel('Signal X(N)')
plt.xlim(n[0],n[-1])
plt.title("0. Signal (Sample domain)")
plt.legend()

N = len(xn)
AF = fs/N
AFn = AF*n

#Establishing time
t = linspace(0, 1, 1000)

#for k in arange(1,11):
    #xt = (4/pi)*((sin(2*pi * (2*k - 1) * 2*t))/(2*k-1))

xt = 4/pi*(sin(2*pi*(2*1-1)*2*t)/(2*1-1))
+ 4/pi*(sin(2*pi*(2*2-1)*2*t)/(2*2-1))\
+ 4/pi*(sin(2*pi*(2*3-1)*2*t)/(2*3-1))\
+ 4/pi*(sin(2*pi*(2*4-1)*2*t)/(2*4-1))\
+ 4/pi*(sin(2*pi*(2*5-1)*2*t)/(2*5-1))\
+ 4/pi*(sin(2*pi*(2*6-1)*2*t)/(2*6-1))\
+ 4/pi*(sin(2*pi*(2*7-1)*2*t)/(2*7-1))\
+ 4/pi*(sin(2*pi*(2*8-1)*2*t)/(2*8-1))\
+ 4/pi*(sin(2*pi*(2*9-1)*2*t)/(2*9-1))\
+ 4/pi*(sin(2*pi*(2*10-1)*2*t)/(2*10-1))

plt.figure()
plt.plot(t, xt)
plt.xlabel('Time (S)')
plt.ylabel('Signal X(S)')
plt.xlim(t[0],t[-1])
plt.title("1. Signal (Time domain)")
plt.legend()

real, imag, mags, angs = mi_dft_func(xn) #Get the DFT for Reals, Imags, Magnitudes and Angles.

#Print the real values.
#plt.figure()
#plt.stem(n, real)
#plt.xlabel('Number of Samples')
#plt.ylabel('Real values X(m)')
#plt.xlim(n[0],n[-1])
#plt.legend()

#Print the imaginary values.
#plt.figure()
#plt.stem(n, imag)
#plt.xlabel('Number of Samples')
#plt.ylabel('Imaginary values X(m)')
#plt.xlim(n[0],n[-1])
#plt.legend()

#Print the Magnitudes
plt.figure()
plt.stem(AFn, mags)
plt.xlabel('Hertz (Hz)')
plt.ylabel('Magnitude values')
plt.xlim(AFn[0],AFn[-1])
plt.title("3. DFT X(m), Magnitudes")
plt.legend()
print(max(xn))
#Print the Angles
plt.figure()
plt.plot(AFn, angs)
plt.xlabel('Hertz (Hz)')
plt.ylabel('Angles')
plt.xlim(AFn[0],AFn[-1])
plt.title("3. DFT X(m), Angles")
plt.legend()

#Return to the X(n) by the IDFT. 
Xm = array(real) + array(imag)*1j
realIDFT,imagIDFT = mi_idft_func(Xm)

#Reals IDFT
plt.figure()
plt.stem(n, realIDFT)
plt.xlabel('Real IDFT X(N)')
plt.ylabel('Number of Samples (N)')
plt.title("4. IDFT X(N) Real")
plt.xlim(n[0],n[-1])
plt.legend()

#Imaginaries IDFT
plt.figure()
plt.stem(n, imagIDFT)
plt.xlabel('Imaginary IDFT X(N)')
plt.ylabel('Number of Samples (N)')
plt.title("4. IDFT X(N) Imaginary")
plt.xlim(n[0],n[-1])
plt.legend()


#Plot X'(N)
t =linspace(0,1,100)
TimeIDFT = (array(realIDFT)/n*ts)*t #Divide by n*ts, multiply by time and voila you are back.

plt.figure()
plt.plot(t, TimeIDFT)
plt.xlabel('Numero de Muestras')
plt.ylabel('X(S)')
plt.xlim(t[0],t[-1])
plt.title("5. IDFT X(S)")
plt.legend()


#Substract X(n) - X'(n)
plt.figure()
plt.stem(n, real-realIDFT)
plt.xlabel('Numero de Muestras')
plt.ylabel('X(N)-X`(N)')
plt.xlim(n[0],n[-1])
plt.title("6. IDFT X(N) - X'(N)")
plt.legend()





