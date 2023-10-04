import OPi.GPIO as GPIO
import time


class Tank:
    def __init__(self):
        # Configure GPIO pins for motor control
        self.motor1_forward_pin = 'PA8'  # Adjust GPIO pin numbers as needed
        self.motor1_backward_pin = 'PA9'
        self.motor2_forward_pin = 'PA10'
        self.motor2_backward_pin = 'PA20'

        GPIO.setmode(GPIO.SUNXI)

        GPIO.setup(self.motor1_forward_pin, GPIO.OUT)
        GPIO.setup(self.motor1_backward_pin, GPIO.OUT)
        GPIO.setup(self.motor2_forward_pin, GPIO.OUT)
        GPIO.setup(self.motor2_backward_pin, GPIO.OUT)

        self.motor1f = GPIO.PWM(self.motor1_forward_pin, 1000)  # 1000 Hz frequency
        self.motor1b = GPIO.PWM(self.motor2_forward_pin, 1000)
        self.motor2f = GPIO.PWM(self.motor1_backward_pin, 1000)  # 1000 Hz frequency
        self.motor2b = GPIO.PWM(self.motor2_backward_pin, 1000)

        self.motor1f.start(50)
        self.motor2f.start(50)
        self.motor1b.start(50)
        self.motor2b.start(50)

    def MOVEFWD(self):
        print('beofre')
        GPIO.output(self.motor1_forward_pin, GPIO.HIGH)
        print("after")
        GPIO.output(self.motor2_forward_pin, GPIO.HIGH)
        print("Hello WOrld")

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
        self.motor1f.ChangeDutyCycle(0)  # Stop PWM
        self.motor2f.ChangeDutyCycle(0)
        self.motor1b.ChangeDutyCycle(0)  # Stop PWM
        self.motor2b.ChangeDutyCycle(0)

    def SETSPEED(self, speed):
        self.motor1f.ChangeDutyCycle(speed)
        self.motor2f.ChangeDutyCycle(speed)
        print("Hello Daniel")

    def cleanup(self):
        GPIO.cleanup()
        self.motor1f.stop()
        self.motor2f.stop()
        self.motor1b.stop()
        self.motor2b.stop()
