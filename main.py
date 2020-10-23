from numpy import cos, sin, pi, arange, zeros, array
import plotly.graph_objects as go
from mi_dft_func import mi_dft_func
from palitos2 import stem_plot

n = arange(0,16)
fs = 16
ts = 1/fs
xn = sin(2*pi*3*n*ts)
N = 8

fig = go.Figure()
fig.add_traces(stem_plot(x=n,y=xn))
fig.update_layout(xaxis=dict(range=[0, len(xn)]))
#fig.show()

real, imag, mags, angs = mi_dft_func(xn)

fig = go.Figure()
fig.add_traces(stem_plot(x=n,y=mags))
fig.update_layout(xaxis=dict(range=[0, len(mags)]))
#fig.show()

fig = go.Figure()
fig.add_traces(stem_plot(x=n,y=angs, color='firebrick'))
fig.update_layout(xaxis=dict(range=[0, len(angs)]))
#fig.show()

vector_zeros = zeros(16) #1012
xn_zeros = array(list(xn) + list(vector_zeros))
n_zeros = arange(0, len(xn_zeros))

fig = go.Figure()
fig.add_traces(stem_plot(x=n_zeros,y=xn_zeros))
fig.update_layout(xaxis=dict(range=[0, len(xn_zeros)]))
#fig.show()

real, imag, mags, angs = mi_dft_func(xn_zeros)

fig = go.Figure()
fig.add_traces(stem_plot(x=n_zeros,y=mags))
fig.update_layout(xaxis=dict(range=[0, len(mags)]))
fig.show()

fig = go.Figure()
fig.add_traces(stem_plot(x=n_zeros,y=angs, color='firebrick'))
#fig.update_layout(xaxis=dict(range=[0, len(angs)]))
fig.update_layout(xaxis=dict(range=[0, len(angs)]), yaxis=dict(range=[-250, 250]))
fig.show()