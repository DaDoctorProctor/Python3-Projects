from numpy import arange, array, cos, pi
import plotly.graph_objects as go
from palitos_2 import stem_plot
from dft_lib_correct import *

file = open("samples_e03.txt", "r")
lines = file.readlines()
file.close()
fs=24
ts=1/fs
samples = []
for line in lines:
	samples.append(float(line))
samples = array(samples)

print("Valores de samples_e03.txt")
print(samples)
#Se imprimen los valores de samples
n = arange(0, len(samples)) #El valor de n va de 0 a 24 ya que la funcion "len(samples)" toma los numeros de datos, que en este caso son 24
fig = go.Figure()
fig.add_traces(stem_plot(x=n/fs, y=samples))
fig.update_layout(title='SEÑAL ORIGINAL', xaxis=dict(range=[0, len(samples)/fs])) #Configuramos el eje horizontal para que sea en orden de la frecuencia
fig.write_html('SEÑAL ORIGINAL.html', auto_open=False)

r,i,m,a=mi_dft(samples)
N=len(samples)
fa=fs/N
#Calculamos la DFT para obtener el angulo y la magnitud

fig=go.Figure()
fig.add_traces(stem_plot(x=n*fa,y=m))
fig.update_layout(title='GRAFICA DE LA MAGNITUD',xaxis=dict(range=[0,N*fa]))#Se configura el eje horizonal para que sea en orden de la frecuencia, se grafica la magnitud

fig.write_html('GRAFICA DE LA MAGNITUD.html', auto_open=False)

fig = go.Figure()
fig.add_traces(stem_plot(x=n*fa, y=a))
fig.update_layout(title='GRAFICA DEL ANGULO', xaxis=dict(range=[0, N*fa]))#Se configura el eje horizonal para que sea en orden de la frecuencia, se grafica el angulo
fig.write_html('GRAFICA DEL ANGULO.html', auto_open=False)

print("Magnitud:")
print(m)
print("Angulo:")
print(a)
#imprimimos los valores de la magnitud y el angulo para cada posición de "m", se calculará con la función "Sum i=0;m-1 A*cos(wn+O)" siendo un total de 24 calculos o x(m)
xnp=(0+cos(2*pi*n*ts-pi/2)+2*cos(4*pi*n*ts)+3*cos(6*pi*n*ts+pi/2)+3*cos(8*pi*n*ts+pi)+2*cos(10*pi*n*ts-pi/2)+cos(12*pi*n*ts-pi/2)+0+0+0+0+0+0+0+0+0+0+0+cos(36*pi*n*ts+pi/2)+2*cos(38*pi*n*ts+pi/2)+3*cos(40*pi*n*ts+pi)+3*cos(42*pi*n*ts-pi/2)+2*cos(44*pi*n*ts)+cos(46*pi*n*ts+pi/2))/2
#El modelo matematico es xnp, esta se obtiene de la forma "Sumatoria i=0;m-1 A cos(wn+O)"
#Este desarrollo viene anexado en el archivo .txt llamado "modelo matematico"
rp,ip,mp,ap=mi_dft(xnp)

fig=go.Figure()
fig.add_traces(stem_plot(x=n*ts,y=xnp))
fig.update_layout(title='GRAFICA DEL MODELO MATEMÁTICO',xaxis=dict(range=[0,1]))
fig.write_html('GRAFICA DEL MODELO MATEMÁTICO.html', auto_open=False)

e=m-mp
#se obtiene la diferencia en las magnitudes de la grafica original y la grafica de nuestro modelo matematico y se grafica con los siguientes comandos
fig=go.Figure()
fig.add_traces(stem_plot(x=n,y=e))
fig.update_layout(title='DIFERENCIA ENTRE LA SEÑAL ORIGINAL Y LA DEL MODELO MATEMÁTICO',xaxis=dict(range=[0,N*fa]), yaxis=dict(range=[-1,1]))
#xaxis=dict(range=[0,N*fa]), yaxis=dict(range=[-1,1])<--- con este comando configuramos el eje X para que sea en frecuencia y el eje y que vaya desde el rango de -1 a 1
#Esto porque el valor es tan pequeño que tiene a 0. si se desea ver la grafica a una precisión exacta se debera de borrar ", yaxis=dict(range=[-1,1])".

fig.write_html('DIFERENCIA ENTRE LA SEÑAL ORIGINAL Y LA DEL MODELO MATEMÁTICO.html', auto_open=False)

print("Diferencia entre señal original y la señal del modelo matematico")
print(e)
#imprime en valores la diferencia.

