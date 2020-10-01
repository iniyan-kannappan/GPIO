import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN)
sensor=GPIO.input(17)
while True:
    sensor=GPIO.input(17)
    if sensor==1:
        print('Not Detected')
        sleep(0.1)
    elif sensor==0:
        print('Detected')
