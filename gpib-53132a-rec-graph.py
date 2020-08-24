# -*- coding: UTF-8 -*-
import visa
import time
import datetime
import pyqtgraph as pg
import numpy as np
import array

app = pg.mkQApp()	#ÁÂ©úÁo

cnt_times=200
device ='GPIB0::3::INSTR'		#agilent 53132a
filename ='file'+time.strftime("%m%d%H%M%S", time.localtime())+'.txt'
rm = visa.ResourceManager()
my_instrument = rm.open_resource(device)
print(my_instrument.query('*IDN?'))
#my_instrument.timeout=0
del my_instrument.timeout

data = array.array('d')
N=200
win=pg.GraphicsWindow()
win.setWindowTitle(u'pyqtgraph')
win.resize(650,400)

p = win.addPlot()
p.showGrid(x=True, y=True)
p.setRange(xRange=[0,N-1], yRange=[-0.002,0.003], padding=0)
p.setLabels(left='tolerence', bottom='times',title='frequency')

curve=p.plot(pen='y')
idx=0
def plotData():
	#global idx
	#tmp=np.sin(np.pi/50*idx)
	meafre = my_instrument.query("FETCH:FREQ?")
	meafre_f = (float(meafre)-1)
	meafre_s = str(meafre_f)
	print (meafre_s)
	
	if len(data)<N:
		data.append(meafre_f)
	else:
		data[:-1]=data[1:]
		data[-1]=meafre_f
		
	curve.setData(data)
	#idx +=1

count=0
filetemp = open (filename, mode='w')
while (count < cnt_times):
	print ((count),'***', datetime.datetime.now())
	meafre = my_instrument.query("FETCH:FREQ?")
	#meafre = my_instrument.query("READ:FREQ?")
	meafre_f = float(meafre)
	meafre_s = str(meafre_f)
	filetemp.write(meafre_s+"\n")	#"\n"
	print (meafre_s)
	print ((meafre_f-1)/meafre_f)
	
	count += 1
filetemp.close
















