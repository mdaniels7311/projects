#!/usr/bin/python
import RPi.GPIO as GPIO, time, math, json

pin = 17
count = 0
count_bucket = 0

def spin(channel):
    global count
    count += 1
    print (count)

def calcspeed():
    r = 9
    t = 5
    CmS = ((math.pi*r)*count)/t
    KmH = (CmS/100000)*3600
    return KmH

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)
GPIO.add_event_detect(pin, GPIO.FALLING, callback=spin, bouncetime=300)

while True:
    count = 0
    time.sleep(5)
    calcspeed()
    windspeed = calcspeed()
    print(windspeed)

from MCP342X import *
adc = MCP342X()

while True:
    print (adc.read(0))
    time.sleep(0.1)

def bucket_tipped(channel):
    global count
    count_bucket += 1
    print (count * 0.2794)

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)
GPIO.add_event_detect(pin, GPIO.FALLING, callback=bucket_tipped, bouncetime=300)
