import RPi.GPIO as GPIO

class servo():

        def __init__():
        
                GPIO.setmode(GPIO.BOARD)
                servoPinx=11
                servoPiny=12
                GPIO.setup(servoPinx, GPIO.OUT)
                GPIO.setup(servoPiny, GPIO.OUT)

                pwmx=GPIO.PWM(servoPinx,50)
                pwmy=GPIO.PWM(servoPiny,50)

                pwmx.start(6.525) #starts in the middle
                pwmy.start(2.486)

# x and y are references to place in image determined by pixels
# desiredAngles are refernces to the current angle that the servos are at
# get x,y from fast and angles from servox/sweep

        def move(x, y, desiredAnglex, desiredAngley):

                if ( (x - 260 > 0) and (240 - y > 0) ):
                {
                        desiredAnglex -= 2
                        desiredAngley += 2
                }

                if ( (240 - x > 0) and (240 - y > 0) ):
                {
                        desiredAnglex = x + 2
                        desiredAngley = y + 2
                }

                if ( (240 - x > 0) and (y - 260 > 0) ):
                {
                        desiredAnglex = x + 2
                        desiredAngley = y - 2
                }
                
                if ( (x - 260 > 0) and (y - 260 > 0) ):
                {
                        desiredAnglex = x - 2
                        desiredAngley = y + 2
                }

                Dx=8.75/180.*(desiredAnglex)+2
                pwmx.ChangeDutyCycle(Dx)
                Dy=8.75/180.*(desiredAngley)+2
                pwmy.ChangeDutyCycle(Dy)

                pwmx.stop()
                pwmy.stop()
                GPIO.cleanup()
