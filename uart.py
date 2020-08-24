# -*- coding: UTF-8 -*-
#ctrl-c 中斷程式
import serial
import time
import datetime

filename ='uart'+time.strftime("%m%d%H%M%S", time.localtime())+'.txt'

#ser = serial.Serial("COM5", 9600, timeout=1)
#print("connected to: " + ser.portstr)



try:
  ser = serial.Serial("COM5", 9600, timeout = 1)
  print ("Port is open")

except serial.SerialException:
  ser.close()
  print ("Port is closed")
  ser = serial.Serial("COM5", 9600, timeout = 1)
  print ("Port is open again")




count=1

filetemp = open (filename, mode='w')
while 1:
#	data = ser.readline()
	data = ser.read(4)

	if (len(data) == 4) :
		head_byte = int(data[0])
		tail_byte = int(data[3])
		adc_high_byte = int(data[1])
		adc_low_byte = int(data[2])
		adc_value = adc_high_byte *256 +adc_low_byte
	
		if (head_byte == 13 and tail_byte == 10):
			adc_value_s = str(adc_value) + "," + str(hex(adc_value))
			print (adc_value_s)
			filetemp.write(adc_value_s+"\n")

	time.sleep(0.1)

ser.close()
filetemp.close 

