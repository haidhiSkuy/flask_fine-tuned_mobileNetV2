import os
from function import *
from ml import predict, confidence_level
from werkzeug.utils import secure_filename
from flask import Flask, flash, request, redirect, render_template, url_for

UPLOAD_FOLDER = "./static"


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = '1a356853413cd128338a7300'


@app.route('/', methods=["GET", "POST"])
def home_page():
    delete_cache()
    if request.method == 'POST': 
        if 'file' not in request.files:
            flash('No file part','danger')
            return redirect(request.url)
        file = request.files['file']
        
        if file.filename == '':
            flash('No selected file', 'warning')
            return redirect(request.url)
        
        if file:
            if allowed_file(file.filename) == False: 
                flash("Please select image file",'error')
                return redirect(request.url)
            
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], "1"+filename)
            file.save(file_path)
            return redirect(url_for('predict_page'))
        
    return render_template("home.html")

@app.route('/predict', methods=["GET", "POST"])
def predict_page(): 
    image = get_image()
    logits, predicted, result = predict(image)
    confidence = confidence_level(logits[0])
    return render_template("predict.html", image=image, confidence=confidence, result=result)


if __name__ == '__main__':
    app.run(host ='0.0.0.0')