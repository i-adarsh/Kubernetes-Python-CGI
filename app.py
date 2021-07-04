from flask import Flask,render_template,request,url_for
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

app=Flask("My_k8s_App")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/docker")
def docker():
    return render_template("docker.html")

@app.route("/kubernetes")
def kubernetes():
    return render_template("kubernetes.html")

@app.route("/teams")
def team():
    return render_template("team.html")

@app.route("/vehicle_detection")
def vehicle_detection():
    return render_template("vehicle_detection.html")


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

UPLOAD_FOLDER = '/Users/adarshkumar/Documents/Flask/Kubernetes-Python-CGI/Files'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return 'Please Select Image File Only'
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return 'No File Selected'
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template("index.html")
#    if request.method == 'POST':
#       f = request.files['file']
#       f.save(secure_filename(f.filename))
#       return 'file uploaded successfully'

if __name__=="__main__":
    app.run(host = "0.0.0.0", port = 5000,debug=True)
