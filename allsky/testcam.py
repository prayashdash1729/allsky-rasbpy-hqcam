import picamera
import time
with picamera.PiCamera() as camera:
	camera.resolution=(640,480)
	camera.start_preview()
	time.sleep(2)

	try:
		while True:
			pass
	except KeyboardInterrupt:
		pass
	
	camera.sop_preview()

  
