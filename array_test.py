# coding=UTF-8
#%matplotlib inline
import visa
import time
import datetime
import numpy as np

N=50
ppsvalue=np.array([5.50, 5.00, 4.5, 3.60, 3.30, 3.00, 2.70, 2.20])

rm = visa.ResourceManager()
pps=rm.open_resource('GPIB0::6::INSTR')
cnter= rm.open_resource('GPIB0::3::INSTR')
print(pps.query('*MODEL?'))
print(cnter.query('*IDN?'))
pps.write ('OVSET1 9.00; OVP 1; OCP 1; ISET1 1.00')
pps.write('VSET1 3.00;OUT1 1')
del cnter.timeout
time.sleep(5)

for ppsv in ppsvalue:
	filename ='file'+time.strftime("%m%d%H%M%S", time.localtime())+'.txt'
	pps.write('VSET1 '+str(ppsv)+';OUT1 1')
	time.sleep(1)

	filetemp = open (filename, mode='a')
	filetemp.write("VDD="+str(ppsv)+"\n")
	filetemp.close	
	#print ('VDD='+str(ppsv))

	fcnt=0
	
	for fcnt in range(N):
		meafre = cnter.query("FETCH:FREQ?")
		filetemp = open (filename, mode='a')
		filetemp.write(str (float(meafre))+"\n")
		filetemp.close	
		print ('VDD=' + str(ppsv) + str((float(meafre)-1)))
		#print (str ((float(meafre)-1)))
			
print ('finished')	
	
