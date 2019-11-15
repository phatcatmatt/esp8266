from gpiozero import LED
import time

red = LED(26)
yellow = LED(19)
green = LED(13)

def off():
	red.off()
	yellow.off()
	green.off()

def rojo():
	red.on()
	yellow.off()
	green.off()

def verde():
	green.on()
	yellow.off()
	red.off()

def amarillo():
	yellow.on()
	red.off()
	yellow.off()


def pong():
	for _ in range (10):
		red.on()
		time.sleep(.1)
		red.off()
		
		yellow.on()
		time.sleep(.1)
		yellow.off()

		green.on()
		time.sleep(.1)
		green.off()

		yellow.on()
		time.sleep(.1)
		yellow.off()
