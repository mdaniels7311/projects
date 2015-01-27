import RPi.GPIO as gp, time, picamera

button = 14
ballon = 2

with picamera.PiCamera() as camera:
    gp.setmode(gp.BCM)
    gp.setwarnings(False)
    gp.setup(button, gp.IN, gp.PUD_UP)
    gp.setup(ballon, gp.OUT)
    print("Ready...")
    gp.wait_for_edge(button, gp.FALLING)
    gp.output(ballon, True)
    time.sleep(5)
    gp.output(ballon, False)
    camera.resolution = (640, 480)
    camera.framerate = 90
    camera.start_preview()
    camera.start_recording('ballon.h264')
    camera.wait_recording(30)
    camera.stop_recording()
    camera.stop_preview()
