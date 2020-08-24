import visa
import time
import datetime
rm = visa.ResourceManager()
my_instrument = rm.open_resource('GPIB0::5::INSTR')
print(my_instrument.query('*IDN?'))

count=0
while (count<101):
	print (count)
	print (datetime.datetime.now())
	print (my_instrument.query('MEASURE:VOLTAGE?'))
	time.sleep(1)
	count+=1
