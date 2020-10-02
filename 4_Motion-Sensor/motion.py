import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
pin=14
GPIO.setup(pin,GPIO.IN)
def LIGHTS(pin):
    print("Motion Detected!")

print("Motion Sensor Alarm (CTRL+C to exit)")
time.sleep(.2)
print("Ready")

try:
    GPIO.add_event_detect(pin,GPIO.RISING,callback=LIGHTS)
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Quit")
    GPIO.cleanup()
