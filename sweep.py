import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
servoPinx=11
GPIO.setup(servoPinx, GPIO.OUT)
pwm=GPIO.PWM(servoPinx,50)

pwm.start(6.525) #starts in the middle
desiredAngle = 90

while(desiredAngle < 180):
        desiredAngle += 4.5
        DC=8.75/180.*(desiredAngle)+2
        pwm.ChangeDutyCycle(DC)
        sleep(.25)
        if (desiredAngle == 180):
                while(desiredAngle > 0):
                        desiredAngle -= 4.5
                        DC=8.75/180.*(desiredAngle)+2
                        pwm.ChangeDutyCycle(DC)
                        sleep(.25)
                        if(desiredAngle == 0):
                                sleep(.25)
                                break
	
pwm.stop()
GPIO.cleanup()
	

