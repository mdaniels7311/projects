import RPi.GPIO as GPIO
import time
import picamera

pin = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, GPIO.PUD_DOWN)

with picamera.PiCamera() as cam:
    cam.resolution = (1024,768)
    while True:
        pin_value = GPIO.input(pin)
        print("HIGH" if pin_value else "LOW")
        time.sleep(0.5)
    if pin_value:
        cam.start_preview() 
        time.sleep(2)
        cam.capture('test.jpeg')
    else:
        print("Press The Button")
