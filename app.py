from flask import Flask, jsonify, request
import os
from deepface import DeepFace
import requests_file

app = Flask(__name__)
models = ["VGG-Face", "Facenet", "Facenet512", "OpenFace", "DeepFace", "DeepID", "ArcFace", "Dlib"]

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/upload', methods=['POST'])
def upload():
   face1 = request.files.get('file')
   face2 = request.files.get('file2')
   randomName = os.urandom(8).hex()
   face1.save(randomName + '.jpg')
   face2.save(randomName + 'face2' + '.jpg')
   result = DeepFace.verify(img1_path=(randomName + '.jpg'), img2_path=(randomName + 'face2' +'.jpg'), model_name = models[2    ])
   return result


if __name__ == '__main__':
    app.run()
