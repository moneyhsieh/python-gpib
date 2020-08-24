# -*- coding: UTF-8 -*-
#ctrl-c 中斷程式

import time
import datetime
import array
import serial
import pyqtgraph as pg
import numpy as np

_comport="COM5"
_baudrate=9600

app = pg.mkQApp()

filename ='uart'+time.strftime("%m%d%H%M%S", time.localtime())+'.txt'

ser = serial.Serial(_comport, _baudrate, timeout=0.1)

data = array.array('d')
N=600
win=pg.GraphicsWindow()
win.setWindowTitle(u'pyqtgraph')
win.resize(650,400)

p = win.addPlot()
p.showGrid(x=True, y=True)
p.setRange(xRange=[0,N-1], yRange=[-10,1050], padding=0)
p.setLabels(left='value', bottom='times',title='10-bit ADC value')

curve=p.plot(pen='y')
idx=0

def plotData():   

    while True:
        uartdata = ser.read(4)
        ws=ser.inWaiting()
        #ser.flushInput()
        if (int(uartdata[0]) == 13 and int(uartdata[3]) == 10):
            adc_value = int(uartdata[1]) *256 + int(uartdata[2])
            adc_value_s = str(adc_value) + "," + str(hex(adc_value))
            print (adc_value_s)
            print (ws)
            filetemp = open (filename, mode='a')
            filetemp.write(adc_value_s+"\n")
            filetemp.close
            break
        else:
            uartdata = ser.read()
            ser.flush()
          
    if len(data)<N:
        data.append(adc_value)
    else:
        data[:-1]=data[1:]
        data[-1]=adc_value
        
    curve.setData(data)
    #time.sleep(0.1) 
timer = pg.QtCore.QTimer()
timer.timeout.connect(plotData)
timer.start(0.001)

app.exec_()
ser.close()

