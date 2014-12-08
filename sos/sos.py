#SOS
import RPi.GPIO as GP,time
GP.setmode(GP.BOARD)
GP.setup(11,GP.OUT)

#defining the function 'dot'
def dot():
    GP.output(11,GP.HIGH)
    time.sleep(0.25)
    GP.output(11,GP.LOW)
    time.sleep(0.5)

#defining the function 'dash'
def dash():
    GP.output(11,GP.HIGH)
    time.sleep(1)
    GP.output(11,GP.LOW)
    time.sleep(0.5)

#this bit will loop forever
while True:
    dot()
    dot()
    dot()
    time.sleep(0.5)
    dash()
    dash()
    dash()
    time.sleep(0.5)
    dot()
    dot()
    dot()
    time.sleep(2)


