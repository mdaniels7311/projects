import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.framerate = 90
    camera.start_preview()
    camera.start_recording('my_video2.h264')
    camera.wait_recording(60)
    camera.stop_recording()
    camera.stop_preview()
