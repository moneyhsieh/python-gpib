# -*- coding: UTF-8 -*-
import visa
import time
import datetime

rm = visa.ResourceManager()
pps=rm.open_resource('GPIB0::6::INSTR')
print(pps.query('*MODEL?'))

while True:
	#pps.write('VSET1 1.0;ISET1 0.1;OUT1 1')
	pps.write('OUT1 0')
	time.sleep(1)
	pps.write('VSET1 1.00;OUT1 1')
	time.sleep(2)
	#pps.write('VSET1 5.0;ISET1 0.1;OUT1 1')
	pps.write('OUT1 0')
	time.sleep(1)
	pps.write('VSET1 5.00;OUT1 1')
	time.sleep(2)
