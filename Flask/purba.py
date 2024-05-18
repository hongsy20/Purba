from flask import Flask, jsonify, request
import requests
import subprocess

app = Flask(__name__)

@app.route('/receiveRequest', methods=['POST'])
def receive_request():
    file = request.files['file'] 
    file.save('Save Photo path') 

    return 'File received successfully!'

if __name__ == '__main__':
    app.run(debug=True)




