import picamera, time

with picamera.PiCamera() as cam:
    cam.resolution = (1024,768)
    cam.start_preview()

    time.sleep(2)
    cam.capture('test.jpeg')
