def mi_dft_func(xn):
	from numpy import pi, sqrt, arctan2, array, arange, e
	N = len(xn)
	n = arange(N)
	X = []
	for m in range(N):
		xne = sum(xn*(e**(-1j*2*pi*m*n/N)))
		#X.append(round(xne, 10) + 0)
		X.append(xne)
	X = array(X)
	X_r = X.real
	X_i = X.imag
	X_m = sqrt(X.real**2+X.imag**2)
	X_a = arctan2(X.imag, X.real)*(180/pi)
	return X_r, X_i, X_m.real, X_a.real

"""
def mi_dft_func(xn):
	from numpy import sin, cos, pi, arange, linspace, arctan2, sqrt, array, round
	reals = []
	imags = []	
	N = len(xn)
	n = arange(N)
	for m in range(N):
		signal_cos = cos(2*pi*m*n/N)
		signal_sin = -sin(2*pi*m*n/N)
		xn_por_cos = xn*signal_cos
		xn_por_sin = xn*signal_sin
		real_part = sum(xn_por_cos)
		imag_part = sum(xn_por_sin)
		reals.append(round(real_part, 10) + 0)
		imags.append(round(imag_part, 10) + 0)
		mags = sqrt(array(reals)**2 + array(imags)**2)
		angs = arctan2(imags,reals)*(180/pi)
	return reals, imags, mags, angs
	"""