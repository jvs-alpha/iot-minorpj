import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(21,GPIO.OUT)

def on():
    GPIO.output(21,True)
    time.sleep(.5)

def off():
    GPIO.output(21,False)
    time.sleep(.5)


if(__name__ == "__main__"):
	on()
	off()
