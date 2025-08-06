from flask import Flask, render_template, request
from scanners.basic_scanner import scan_document
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    file = request.files['document']
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    result = scan_document(file_path)
    os.remove(file_path)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
