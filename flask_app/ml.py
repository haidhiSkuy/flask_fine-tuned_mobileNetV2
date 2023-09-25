import cv2 as cv
import numpy as np
import tensorflow as tf
from keras.preprocessing import image


model = tf.keras.models.load_model('animal.h5')
label = {0: 'Butterfly', 
         1: 'Cat', 
         2: 'Cow', 
         3: 'Dog', 
         4: 'Elephant',
         5: 'Hen', 
         6: 'Horse', 
         7: 'Sheep', 
         8: 'Spider', 
         9: 'Squirrel'}


def predict(image_path):
    path = image_path
    img = image.load_img(path, target_size=(160, 160))
    img = image.img_to_array(img)
    img = img.reshape((160, 160, 3))
    img = img / 255.0  # Normalize pixel values
    img = np.expand_dims(img, axis=0)

    logits = model.predict(img)
    predicted = np.argmax(logits)
    result = label[predicted]

    return logits, predicted, result 

def confidence_level(logits): 
    confidence = {}
    for val, logit in zip(label.values(), logits):
        formatted_num = "{:.2f}".format(logit*100)
        confidence[val] = formatted_num + "%"
    return confidence


