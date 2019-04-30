#!/usr/local/bin/python3
from flask import Flask, request, render_template, make_response, jsonify, json
from facenet.src.align import detect_face
from scipy import misc

import tensorflow as tf
import cv2
import numpy as np
import base64


app = Flask(__name__)

def get_img_and_bounding_boxes(img, minsize, threshold, factor):   
    with tf.Graph().as_default():
        sess = tf.Session()
        with sess.as_default():
            pnet, rnet, onet = detect_face.create_mtcnn(sess, None)

    bounding_boxes, _ = detect_face.detect_face(img, minsize, pnet, rnet, onet, threshold, factor)

    for (x1, y1, x2, y2, acc) in bounding_boxes:
        img = cv2.rectangle(img,(int(x1),int(y1)),(int(x2), int(y2)),(255,0,0),2)

    return img, bounding_boxes        


@app.route("/upload", methods=['POST'])
def upload():
    file = request.files['inputFile']
    img_io = file.read()

    try:
        minsize = float(request.form["minsize"])
    except:
        minsize = 40.0 

    try:
        threshold = [float(x) for x in request.form["threshold"].split(',')]
    except:
        threshold = [0.6, 0.7, 0.7]

    try:
        factor = float(request.form["factor"])
    except:
        factor = 0.7 


    np_img = np.fromstring(img_io, np.uint8)
    cv2_img = cv2.imdecode(np_img, cv2.IMREAD_UNCHANGED)
    
    img_with_bounding_box, bounding_boxes = get_img_and_bounding_boxes(cv2_img, minsize, threshold, factor)

    if request.form['submit_button'] == 'image' and bounding_boxes.size != 0:
        _, buffer = cv2.imencode('.png', img_with_bounding_box)

        response = make_response(buffer.tobytes())
        response.headers['Content-Type'] = 'image/png'
    
        return response
    elif request.form['submit_button'] == 'json' and bounding_boxes.size != 0:
        return jsonify(
            boundingBox=[{"x1": x[0], "y1": x[1], "x2": x[2], "y2": x[3], "acc": x[4]} for x in bounding_boxes.tolist()],
            fileName=file.filename,
            status="Succeeded"
        )
    else:
        return jsonify(
            fileName=file.filename,
            status="Failed",
            description="Failed or no Face in Image"
        )

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')