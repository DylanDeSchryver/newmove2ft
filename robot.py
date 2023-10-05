import RPi.GPIO as GPIO
import time

class RobotClass:
    def __init__(self):
        # Configure GPIO pins for motor control
        self.motor1_enable_pin = 'PA8'  # PWM pin for motor 1
        self.motor1_forward_pin = 'PA9'
        self.motor1_backward_pin = 'PA10'
        self.motor2_enable_pin = 'PA20'  # PWM pin for motor 2
        self.motor2_forward_pin = 'PA21'
        self.motor2_backward_pin = 'PA22'

        #set move to sunxi numbering (PA#)
        GPIO.setmode(GPIO.SUNXI)
        GPIO.setup(self.motor1_forward_pin, GPIO.OUT)
        GPIO.setup(self.motor1_backward_pin, GPIO.OUT)
        GPIO.setup(self.motor2_forward_pin, GPIO.OUT)
        GPIO.setup(self.motor2_backward_pin, GPIO.OUT)

        # Initialize PWM pins for motor speed control
        GPIO.setup(self.motor1_enable_pin, GPIO.OUT)
        GPIO.setup(self.motor2_enable_pin, GPIO.OUT)
        self.motor1_pwm = GPIO.PWM(self.motor1_enable_pin, 1000)  # 1000 Hz frequency
        self.motor2_pwm = GPIO.PWM(self.motor2_enable_pin, 1000)

        # Start PWM with 0% duty cycle (motors stopped)
        self.motor1_pwm.start(0)
        self.motor2_pwm.start(0)

    def MOVEFWD(self, speed):
        # Set the direction pins for forward motion
        GPIO.output(self.motor1_forward_pin, GPIO.HIGH)
        GPIO.output(self.motor2_forward_pin, GPIO.HIGH)
        GPIO.output(self.motor1_backward_pin, GPIO.LOW)
        GPIO.output(self.motor2_backward_pin, GPIO.LOW)

        # Set the speed for forward motion (0 to 100%)
        self.SETSPEED(speed)

    def SETSPEED(self, speed):
        # Set motor speed using PWM (speed: 0 to 100)
        self.motor1_pwm.ChangeDutyCycle(speed)
        self.motor2_pwm.ChangeDutyCycle(speed)
        print("Hello Daneil")

    def MOVEBACKWARD(self):
        GPIO.output(self.motor1_forward_pin, GPIO.LOW)
        GPIO.output(self.motor2_forward_pin, GPIO.LOW)
        GPIO.output(self.motor1_backward_pin, GPIO.HIGH)
        GPIO.output(self.motor2_backward_pin, GPIO.HIGH)

    def TURNLEFT(self):
        GPIO.output(self.motor1_forward_pin, GPIO.LOW)
        GPIO.output(self.motor2_forward_pin, GPIO.HIGH)
        GPIO.output(self.motor1_backward_pin, GPIO.HIGH)
        GPIO.output(self.motor2_backward_pin, GPIO.LOW)

    def TURNRIGHT(self):
        GPIO.output(self.motor1_forward_pin, GPIO.HIGH)
        GPIO.output(self.motor2_forward_pin, GPIO.LOW)
        GPIO.output(self.motor1_backward_pin, GPIO.LOW)
        GPIO.output(self.motor2_backward_pin, GPIO.HIGH)

    def STOP(self):
        GPIO.output(self.motor1_forward_pin, GPIO.LOW)
        GPIO.output(self.motor2_forward_pin, GPIO.LOW)
        GPIO.output(self.motor1_backward_pin, GPIO.LOW)
        GPIO.output(self.motor2_backward_pin, GPIO.LOW)
        self.motor1_pwm.ChangeDutyCycle(0)  # Stop PWM
        self.motor2_pwm.ChangeDutyCycle(0)





    def cleanup(self):
        # Clean up GPIO settings and PWM
        GPIO.cleanup()
        self.motor1_pwm.stop()
        self.motor2_pwm.stop()

