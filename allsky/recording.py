import picamera
import io
import time

camera = picamera.PiCamera()

def record_video():
    camera.resolution = (640, 480)
    camera.framerate = .5        
    camera.exposure_mode = 'off'  # Turn off automatic exposure
    camera.shutter_speed = 100*10  # Convert ms to µs
        
    camera.start_recording("test.mp4", format='h264')  

if __name__ == '__main__':
    record_video()
    time.sleep(10)
    camera.stop_recording()
