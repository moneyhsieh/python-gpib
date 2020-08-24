# -*- coding: UTF-8 -*-
import visa
import time
import datetime

cnt_times=200
device ='GPIB0::3::INSTR'		#agilent 53132a
filename ='file'+time.strftime("%m%d%H%M%S", time.localtime())+'.txt'
rm = visa.ResourceManager()
my_instrument = rm.open_resource(device)
print(my_instrument.query('*IDN?'))
#my_instrument.timeout=0
del my_instrument.timeout
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
