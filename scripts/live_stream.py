#!/usr/bin/env python
#credit:https://github.com/miguelgrinberg/flask-video-streaming
import os
import cv2
from importlib import import_module
from flask import Flask, render_template, Response
app = Flask(__name__)

@app.route('/')
def index():
    """Video streaming home page."""
    return """
    <html>
  <head>
    <title>Video Streaming Demonstration</title>
  </head>
  <body>
    <h1>Video Streaming Demonstration</h1>
    <img src="/video_feed">
  </body>
</html>
    """

def toJPGNBytes(frame):
    return cv2.imencode('.jpg',frame )[1].tobytes()

def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = toJPGNBytes(camera.read()[1])
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    if __name__=="__main__":
        return Response(gen(camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
    else:
        global frame
        return Response(toJPGNBytes(frame),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    camera = cv2.VideoCapture(0)
    app.run(host='0.0.0.0', threaded=True)
