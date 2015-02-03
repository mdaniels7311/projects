#Imports time and the GPIO modules
import RPi.GPIO as GPIO
import time

#Sets the variable 'Pin' to have a value of 4
pin = 27
#Sets up the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)

count = 0
current_state = 0
previous_state = 0

#Reads if the pin is pressed or not and prints out the result
while True:
    current_state = GPIO.input(pin)

    if previous_state == GPIO.HIGH and current_state == GPIO.LOW:
        count += 1
        print (count)

    previous_state = current_state
    time.sleep(0.01)
