# coding=UTF-8
#%matplotlib inline
# editor: marks
import visa
import time
import datetime
import numpy as np

N=20
ppsvalue=np.array([5.50, 5.00, 4.50, 3.60, 3.30, 3.00, 2.70, 2.20, 2.00, 1.80, 1.50, 1.20, 1.10, 1.00])
#ppsvalue=np.array([2.20, 1.80, 1.60, 1.40, 1.30, 1.20, 1.10, 1.00, 0.90])
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
	filename ='v-f-10_'+time.strftime("%m%d%H%M%S", time.localtime())+'.txt'
	pps.write('VSET1 '+str(ppsv)+';OUT1 1')
	time.sleep(10)

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
pps.close()
cnter.close()

	
