from flask import Flask, render_template, Response, request, redirect
import picamera
import io

app = Flask(__name__, template_folder='Templates')

camera = None  # Initialize camera as None

def initialize_camera():
    global camera
    if camera is None:
        try:
            camera = picamera.PiCamera()
            camera.resolution = (640, 480)
            camera.framerate = 30
        except picamera.PiCameraError as e:
            return str(e)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update_settings', methods=['POST'])
def update_settings():
    error_message = initialize_camera()  # Initialize the camera if not already done

    if error_message:
        return f"Error: {error_message}"

    # Get user input from the form
    resolution = request.form['resolution']
    framerate = request.form['framerate']

    # Validate and update camera settings
    try:
        width, height = map(int, resolution.split('x'))
        camera.resolution = (width, height)
        camera.framerate = int(framerate)
    except ValueError:
        return "Invalid input. Please enter resolution as 'widthxheight' and framerate as an integer."
    except picamera.PiCameraError as e:
        return str(e)

    return redirect('/')

def generate_frames():
    initialize_camera()  # Initialize the camera if not already done

    while True:
        stream = io.BytesIO()
        try:
            camera.capture(stream, 'jpeg')
            stream.seek(0)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + stream.read() + b'\r\n')
        except picamera.PiCameraError as e:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + str(e).encode() + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
