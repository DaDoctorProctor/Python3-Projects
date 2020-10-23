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