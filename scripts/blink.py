#https://www.element14.com/community/thread/58117/l/raspberry-pi-3-gpio-not-working?displayFullThread=true

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

GPIO.setwarnings(True) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(38, GPIO.OUT, initial=GPIO.LOW) # Blue LED
GPIO.setup(36, GPIO.OUT, initial=GPIO.LOW) # RED LED
GPIO.setup(40, GPIO.OUT, initial=GPIO.LOW) # Buzzer LED

def eyeAlert(s):
    blue1()
    sleep(s)
    blue0()

def blue1():
    GPIO.output(38, GPIO.HIGH)
def blue0():
    GPIO.output(38, GPIO.LOW)

def DrownAlert(s):
    red1()
    sleep(s)
    red0()

def red1():
    GPIO.output(36, GPIO.HIGH)

def red0():
    GPIO.output(36, GPIO.LOW)

    
def Buzz(s):
    buzz1() 
    sleep(s)
    buzz0()

def buzz1():
    GPIO.output(40,GPIO.HIGH)

def buzz0():
    GPIO.output(40,GPIO.LOW)

if __name__=="__main__":
    try:
        while True: # Run forever
            Buzz(1)
            eyeAlert(1)
            DrownAlert(1)
    except KeyboardInterrupt:
        GPIO.cleanup()
