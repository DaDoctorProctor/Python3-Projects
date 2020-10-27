import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack as fft

plt.rcParams['figure.figsize'] = [16,12]
plt.rcParams.update({'font.size':18})

from scipy.io import wavfile 

import gc 
gc.collect()

#Create signal
dt = 0.001
t = np.arange(0,1,dt)
fs,Data = wavfile.read('AUDIO.wav')

xn = Data
n = np.arange(0, len(xn))
nfs = n/fs

##Compute FFT

n = len(Data)
fhat = fft.fft(Data) 
PSD = fhat * np.conj(fhat) / n #Power spectrum.
freq = (1/(dt*n)) * np.arange(n) #X axis of frequencies in Hz.
L = np.arange(1,np.floor(n/2),dtype='int') #Compute half of the transform.
print(freq)

plt.figure()
plt.plot(nfs,xn,color='c')
plt.xlabel('Time (S)')
plt.ylabel('Frequency (kHz)')
plt.title('Audio Sample')
plt.xlim(nfs[0],nfs[-1])
plt.legend()

plt.figure()
plt.plot(freq[L],PSD[L],color='r')
plt.xlabel('Frequency (Hz)')
plt.ylabel('PSD')
plt.title('FFT')
plt.xlim(freq[L[0]],freq[L[-1]])
plt.legend()


from numpy import real,imag,sqrt
newidft = fft.ifft(PSD)
realidftx = real(newidft)

from scipy.io.wavfile import write
samplerate = fs

write("ApplyingIFFT.wav", samplerate,realidftx)
plt.show()