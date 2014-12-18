import picamera, time

with picamera.PiCamera() as cam:
    cam.resolution = (1024,768) #sets the camera resolution
    cam.start_preview() #starts the camera view

    time.sleep(2) #waits 2 seconds then takes picture
    cam.capture('test.jpeg')
