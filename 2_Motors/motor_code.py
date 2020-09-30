from gpiozero import Motor
from time import sleep
motor1=Motor(14,15)
motor2=Motor(23,24)
for x in range(4):
    motor2.backward()
    sleep(2)
    motor1.forward()
    sleep(2)
    motor1.stop()
    motor2.stop()
