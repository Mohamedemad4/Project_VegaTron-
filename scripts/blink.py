#https://www.element14.com/community/thread/58117/l/raspberry-pi-3-gpio-not-working?displayFullThread=true
try:
    import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
    GPIO.setwarnings(True) # Ignore warning for now
    GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
    GPIO.setup(38, GPIO.OUT, initial=GPIO.LOW) # Blue LED
    GPIO.setup(36, GPIO.OUT, initial=GPIO.LOW) # RED LED
    GPIO.setup(40, GPIO.OUT, initial=GPIO.LOW) # Buzzer LED
    dbg=False
except ImportError:
    print("couldn't import RPi.GPIO")
    print("running on DEBUG mode")
    dbg=True

from time import sleep

def eyeAlert(s):
    blue1()
    sleep(s)
    blue0()

def blue1():
    if not dbg:
        GPIO.output(38, GPIO.HIGH)
    else:
        print("Blue on")

def blue0():
    if not dbg:
        GPIO.output(38, GPIO.LOW)
    else:
        print("Blue off")

def DrownAlert(s):
    red1()
    sleep(s)
    red0()

def red1():
    if not dbg:
        GPIO.output(36, GPIO.HIGH)
    else:
        print("red one")

def red0():
    if not dbg:
        GPIO.output(36, GPIO.LOW)
    else:
        print("red zero")
    
def Buzz(s):
    buzz1() 
    sleep(s)
    buzz0()

def buzz1():
    if not dbg:
        GPIO.output(40,GPIO.HIGH)
    else:
        print("Buzzer on")

def buzz0():
    if not dbg:
        GPIO.output(40,GPIO.LOW)
    else:
        print("Buzzer off")

if __name__=="__main__":
    try:
        while True: # Run forever
            Buzz(1)
            eyeAlert(1)
            DrownAlert(1)
    except KeyboardInterrupt:
        GPIO.cleanup()
