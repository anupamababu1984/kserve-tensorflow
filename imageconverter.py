
import json
import numpy as np
from PIL import Image
from tensorflow.keras.preprocessing import image

def preprocess_image(image_path):
    img = image.load_img(image_path, target_size=(224, 224))  # Adjust size as per your model
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0  # Normalize if required
    return img_array

def convert_to_json(image_path):
    img_array = preprocess_image(image_path)
    data = {
        "instances": img_array.tolist()
    }
    with open('input.json', 'w') as json_file:
        json.dump(data, json_file)

# Usage
convert_to_json('C:/Users/awsli/kserve-tensorflow/ben2.jpg')
