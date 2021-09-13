#!/usr/bin/python

import RPi.GPIO as GPIO
import time

class gpio_scan:


	_GPIO_APN_6  = 26 # scan_clk
	_GPIO_APN_1  = 20 # scan_enable
	_GPIO_APN_10 = 19 # scan_in_1
	_GPIO_APN_9  = 21 # scan_in_2
	_GPIO_APN_7  = 13 # scan_in_3
	_GPIO_APN_2  = 6  # scan_in_4
	_GPIO_APN_4  = 16 # scan_out_1
	_GPIO_APN_5  = 12 # scan_out_2
	_GPIO_APN_3  = 7  # scan_out_3
	_GPIO_APN_8  = 8  # scan_out_4
	
	def __init__(self, debug=False):
		self.debug = debug
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BCM) # B+ Wedge pin-numbering scheme

		GPIO.setup(self._GPIO_APN_6,  GPIO.OUT, initial=GPIO.HIGH)
		GPIO.setup(self._GPIO_APN_1,  GPIO.OUT, initial=GPIO.LOW)
		GPIO.setup(self._GPIO_APN_10, GPIO.OUT, initial=GPIO.HIGH)
		GPIO.setup(self._GPIO_APN_9,  GPIO.OUT, initial=GPIO.HIGH)
		GPIO.setup(self._GPIO_APN_7,  GPIO.OUT, initial=GPIO.HIGH)
		GPIO.setup(self._GPIO_APN_2,  GPIO.OUT, initial=GPIO.LOW)
#		GPIO.setup(self._GPIO_APN_4,  GPIO.IN,  pull_up_down=GPIO.PUD_DOWN)
#		GPIO.setup(self._GPIO_APN_5,  GPIO.IN,  pull_up_down=GPIO.PUD_DOWN)
#		GPIO.setup(self._GPIO_APN_3,  GPIO.IN,  pull_up_down=GPIO.PUD_DOWN)
		GPIO.setup(self._GPIO_APN_4,  GPIO.IN)
		GPIO.setup(self._GPIO_APN_5,  GPIO.IN)
		GPIO.setup(self._GPIO_APN_3,  GPIO.IN)
		GPIO.setup(self._GPIO_APN_8,  GPIO.IN,  pull_up_down=GPIO.PUD_DOWN)

		
	
	def load_and_compare_list(self, pat_name='0', pattern=[], shift=False):
		list_APN_1  = []
		list_APN_1  = pattern[0]
		list_APN_2  = []
		list_APN_2  = pattern[1]
		list_APN_3  = []
		list_APN_3  = pattern[2]
		list_APN_4  = []
		list_APN_4  = pattern[3]
		list_APN_5  = []
		list_APN_5  = pattern[4]
		list_APN_6  = []
		list_APN_6  = pattern[5]
		list_APN_7  = []
		list_APN_7  = pattern[6]
		list_APN_9  = []
		list_APN_9  = pattern[7]
		list_APN_10 = []
		list_APN_10 = pattern[8]
		list_APN_8  = []
		list_APN_8  = pattern[9]
		
		print "--> Driving Pattern %s <--" % pat_name
		for index in range(0, len(list_APN_9)):
			
			# Compares come before driving data and clocking
			if (list_APN_4[index] == 'H' and GPIO.input(self._GPIO_APN_4) != 1):
				print "Pattern %s :Miscompare on APN_4 at index %d, expected a high but saw a low" % (pat_name,index)
			elif (list_APN_4[index] == 'L' and GPIO.input(self._GPIO_APN_4) != 0):
				print "Pattern %s :Miscompare on APN_4 at index %d, expected a low but saw a high" % (pat_name,index)
			if (list_APN_5[index] == 'H' and GPIO.input(self._GPIO_APN_5) != 1):
				print "Pattern %s :Miscompare on APN_5 at index %d, expected a high but saw a low" % (pat_name,index)
			elif (list_APN_5[index] == 'L' and GPIO.input(self._GPIO_APN_5) != 0):
				print "Pattern %s :Miscompare on APN_5 at index %d, expected a low but saw a high" % (pat_name,index)
			if (list_APN_3[index] == 'H' and GPIO.input(self._GPIO_APN_3) != 1):
				print "Pattern %s :Miscompare on APN_3 at index %d, expected a high but saw a low" % (pat_name,index)
			elif (list_APN_3[index] == 'L' and GPIO.input(self._GPIO_APN_3) != 0):
				print "Pattern %s :Miscompare on APN_3 at index %d, expected a low but saw a high" % (pat_name,index)
			if (list_APN_8[index] == 'H' and GPIO.input(self._GPIO_APN_8) != 1):
				print "Pattern %s :Miscompare on APN_8 at index %d, expected a high but saw a low" % (pat_name,index)
			elif (list_APN_8[index] == 'L' and GPIO.input(self._GPIO_APN_8) != 0):
				print "Pattern %s :Miscompare on APN_8 at index %d, expected a low but saw a high" % (pat_name,index)
			
			if (list_APN_1[index] == 1):
				GPIO.output(self._GPIO_APN_1,  GPIO.HIGH)
			else:
				GPIO.output(self._GPIO_APN_1,  GPIO.LOW)
			if (list_APN_10[index] == 1):
				GPIO.output(self._GPIO_APN_10, GPIO.HIGH)
			else:
				GPIO.output(self._GPIO_APN_10, GPIO.LOW)
			if (list_APN_9[index] == 1):
				GPIO.output(self._GPIO_APN_9,  GPIO.HIGH)
			else:
				GPIO.output(self._GPIO_APN_9,  GPIO.LOW)
			if (list_APN_7[index] == 1):
				GPIO.output(self._GPIO_APN_7,  GPIO.HIGH)
			else:
				GPIO.output(self._GPIO_APN_7,  GPIO.LOW)
			if (list_APN_2[index] == 1):
				GPIO.output(self._GPIO_APN_2,  GPIO.HIGH)
			else:
				GPIO.output(self._GPIO_APN_2,  GPIO.LOW)
			if (list_APN_6[index] == 0):                  #APN_6 is the scan clock, so it needs to driven last
				GPIO.output(self._GPIO_APN_6,  GPIO.LOW)
			else:
				GPIO.output(self._GPIO_APN_6,  GPIO.HIGH)
			time.sleep(0.0000001)
			if (shift == True and list_APN_6[index] == 1): # drive scan clock low if it was just driven high, only for shift patterns
				GPIO.output(self._GPIO_APN_6,  GPIO.LOW)
				
			
