import RPi.GPIO as gp

gp.setmode(gp.BCM)
gp.setwarnings(False)
button = 14
gp.setup(button, gp.IN, gp.PUD_UP)
