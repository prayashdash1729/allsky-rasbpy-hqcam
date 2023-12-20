from flask import Flask, render_template, Response, request
import picamera
import io
import os
from datetime import datetime

timelapse = False;
auto = False;


def make_dir():
    global image_directory
    image_directory = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    if not os.path.exists(image_directory):
        os.makedirs(image_directory)
    
def save_image(image_data):
    global image_directory
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_path = os.path.join(image_directory, "_" + f"{timestamp}.jpg")

    with open(file_path, 'wb') as f:
        f.write(image_data)
        
            
def generate_frames():
    
    camera = picamera.PiCamera(resolution = (1280, 720), framerate=0.16, sensor_mode=3)
    
    if not auto:
        camera.shutter_speed = 6000000  # In µs, 0 denotes auto exposure.
        camera.iso = 1600
        camera.exposure_mode = 'off'  # Turn off automatic exposure
        
        
    while True:
        stream = io.BytesIO()
        camera.capture(stream, 'jpeg')
        stream.seek(0)
        stream_out = stream.read()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + stream_out + b'\r\n')
        if timelapse:
            save_image(stream_out)



app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    
    if timelapse:
        make_dir()

    return render_template('index.html', video_feed=generate_frames())


@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
