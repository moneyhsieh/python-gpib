# -*- coding: UTF-8 -*-
import pyqtgraph as pg
import numpy as np
import array
import visa
import time
import datetime

filename ='file'+time.strftime("%m%d%H%M%S", time.localtime())+'.txt'

device ='GPIB0::3::INSTR'		#agilent 53132a

app = pg.mkQApp()	

rm = visa.ResourceManager()
my_instrument = rm.open_resource(device)
print(my_instrument.query('*IDN?'))
#my_instrument.timeout=10000
del my_instrument.timeout

data = array.array('d')
N=500
win=pg.GraphicsWindow()
win.setWindowTitle(u'53132A frequency')
win.resize(650,480)

p = win.addPlot()
p.showGrid(x=True, y=True)
p.setRange(xRange=[0,N-1], yRange=[-0.0031,0.0031], padding=0.0005)
p.setLabels(left='tolerence', bottom='times',title='frequency')

curve=p.plot(pen='y')
#idx=0

def plotData():
	#global idx
	#tmp=np.sin(np.pi/50*idx)
	meafre = my_instrument.query("FETCH:FREQ?")
	meafre_f = (float(meafre)-1)
	meafre_s = str(meafre_f)

	filetemp = open (filename, mode='a')
	filetemp.write(str (float(meafre))+"\n")
	filetemp.close	
	
	print ('percent:{:.4%}'.format(float(meafre)-1))
	
	if len(data)<N:
		data.append(meafre_f)
	else:
		data[:-1]=data[1:]
		data[-1]=meafre_f
		
	curve.setData(data)
	#idx +=1
	
timer = pg.QtCore.QTimer()
timer.timeout.connect(plotData)
timer.start(100)

app.exec_()
