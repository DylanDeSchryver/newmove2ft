import robot
import time
import OPi.GPIO as GPIO



tank = robot.RobotClass()

tank.STOP()
tank.MOVEFWD(50)
time.sleep(5)
tank.STOP()
GPIO.cleanup()
