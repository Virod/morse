
import RPi.GPIO as GPIO    

import time 

PIN = 7

GPIO.setmode(GPIO.BOARD)  


GPIO.setup(PIN, GPIO.OUT)    


dict = 	{
	"a" : "-",
	'b' : "-...", 
	'c' : "-.-.",
	'd' : "-..",
	'e' : ".",
	'f' : "..-.",
	'g' : "--.",
	'h' : "....",
	'i' : "..",
	'j' : ".---", 
	'k' : "-.-",
	'l' : "..",
	'm' : "--",
	'n' : "-.",
	'o' : "---",
	'p' : ".--.",
	'q' : "--.-",
	'r' : ".-.",
	's' : "...",
	't' : "-",
	'u' : "..-" ,
	'v' : "...-",
	'w' : ".--",
	'x' : "-..-",
	'y' : "-.--",
	'z' : "--.."
}

def dot():
  	GPIO.output(PIN, 1)      
	print ("ON")
	time.sleep(0.2)  
	GPIO.output(PIN, 0)

def dash():
 	GPIO.output(PIN, 1)
	print("ONN")   
 	time.sleep(0.6) 
 	GPIO.output(PIN, 0) 

try:
	input = raw_input
except NameError:
	pass

while True:
	s = input("s = ")
	if s == "exit":
		break
	for a in s:
		print(a)
		code = dict [a]
		# print (code)
		
		for el in code:
			print(el)
			if el == ".":
				dot()
			else :
				dash()
			time.sleep(0.2)  
		time.sleep(0.2)





	