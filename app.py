from flask import Flask, render_template, request
from tensorflow.keras.preprocessing import image
import numpy as np
from tensorflow.keras.models import load_model
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
model = load_model('dogvscat.h5.keras')

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)
    img = image.load_img(file_path, target_size=(200, 200))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    result = model.predict(img)
    if result >= 0.5:
        prediction = 'Dog'
    else:
        prediction = 'Cat'

    # Remove the uploaded file after prediction
    os.remove(file_path)

    return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
