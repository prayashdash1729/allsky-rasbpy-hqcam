from flask import Flask, render_template, Response
import picamera
import io

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

def generate_frames():
    camera = picamera.PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = .5        
    camera.exposure_mode = 'off'  # Turn off automatic exposure
    camera.shutter_speed = 100*10  # Convert ms to µs
        
    while True:
        stream = io.BytesIO()
        camera.capture(stream, 'jpeg')
        stream.seek(0)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + stream.read() + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
