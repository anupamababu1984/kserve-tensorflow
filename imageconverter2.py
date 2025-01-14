import numpy as np
import matplotlib.pyplot as plt
import json
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

def preprocess_image(ct_image_path):
    # Load CT scan image data
    ct_scan_data = plt.imread(ct_image_path)

    # Ensure the correct shape for the CT scan image data
    ct_scan_data = image.img_to_array(ct_scan_data)
    ct_scan_data = preprocess_input(ct_scan_data)
    ct_scan_data = np.expand_dims(ct_scan_data, axis=0)  # Add batch dimension
    return ct_scan_data

def convert_to_json(ct_image_path):
    img_array = preprocess_image(ct_image_path)
    data = {
        "instances": img_array.tolist()
    }
    with open('input.json', 'w') as json_file:
        json.dump(data, json_file)

# Usage
convert_to_json('C:/Users/awsli/kserve-tensorflow/squamous.png')
