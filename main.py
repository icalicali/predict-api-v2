import os
from google.cloud import storage
import tensorflow as tf
from io import BytesIO
from flask import Flask, request, jsonify
from keras.models import load_model
import numpy as np
from tensorflow.keras.applications.mobilenet import preprocess_input
from tensorflow.keras.preprocessing.image import load_img, img_to_array

app = Flask(__name__)
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'credentials.json'
storage_client = storage.Client()


def req(y_true, y_pred):
    req = tf.metrics.req(y_true, y_pred)[1]
    tf.keras.backend.get_session().run(tf.local_variables_initializer())
    return req

def predict_image(image_path):
    image = load_img(image_path, target_size=(299, 299))
    image_array = img_to_array(image)/255
    image_array = tf.expand_dims(image_array, axis=0)
    return model.predict(image_array)

class_label = {0: 'Kertas', 1: 'Botol Plastik', 2: 'Botol Kaca', 3: 'Kaleng', 4:'Kerdus'}

model = load_model('my_model_fix.h5', custom_objects={'req': req})

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            image_bucket = storage_client.get_bucket(
                'trashure-app')
            filename = request.json['filename']
            img_blob = image_bucket.blob('predict_uploads/' + filename)
            img_path = BytesIO(img_blob.download_as_bytes())
            preds = predict_image(img_path)
        except Exception:
            respond = jsonify({'message': 'Error loading image file'})
            respond.status_code = 400
            return respond

        result = {
            'predictions':str(preds[0]),
            'jenis_sampah': class_label[np.argmax(preds)],
        }

        respond = jsonify(result)
        respond.status_code = 200
        return respond

    return 'OK'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')