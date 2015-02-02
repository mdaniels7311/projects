#Imports time and the GPIO modules
import RPi.GPIO as GPIO
import time

#Sets the variable 'Pin' to have a value of 4
pin = 4

#Sets up the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)

#Reads if the pin is pressed or not and prints out the result
while True:
    pin_value = GPIO.input(pin)
    print("HIGH" if pin_value else "LOW")
    time.sleep(0.1)
