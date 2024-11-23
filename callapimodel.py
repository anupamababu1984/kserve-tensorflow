import requests
import json
import numpy as np
import sys
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

image_name = sys.argv[1]
print(image_name)

#ct_image_path = r"C:\\Users\\awsli\\kserve-tensorflow\\ben3.jpg"
ct_image_path = r"C:\\Users\\awsli\\kserve-tensorflow\\" + image_name

# Load CT scan image data
ct_scan_data = plt.imread(ct_image_path)

# Ensure the correct shape for the CT scan image data
ct_scan_data = image.img_to_array(ct_scan_data)
ct_scan_data = preprocess_input(ct_scan_data)
ct_scan_data = np.expand_dims(ct_scan_data, axis=0)  # Add batch dimension

json_data = {
        "instances": ct_scan_data.tolist()
    }

# Set your variables
service_hostname = "tensorflow-from-uri-gzip.default.example.com"
ingress_host = "localhost"
ingress_port = "8080"
model_name = "tensorflow-from-uri-gzip"
#input_path = r"C:\\Users\\awsli\\kserve-tensorflow\\input.json"  # Replace this with your actual input data or path


#try:
#    with open(input_path, 'r') as file:
#        json_data = json.load(file)  # This will load the JSON as an object

#except FileNotFoundError:
#    print(f"File not found: {input_path}")
#    exit(1)

# Define the headers
headers = {
    "Host": service_hostname,
    "Content-Type": "application/json",  # Ensure this matches your API's expected content type
}

# Construct the URL
url = f"http://{ingress_host}:{ingress_port}/v1/models/{model_name}:predict"

# Make the request
response = requests.post(url, headers=headers, json=json_data)

# Print the response
print("Status Code:", response.status_code)

response_body = response.json()

# Make predictions using the CT model
predictions_ct = response_body['predictions']
print(predictions_ct)

# Get probabilities for each class
probability_benign = predictions_ct[0][0]
probability_malignant = predictions_ct[0][1]

# Determine the class with the highest probability
class_labels = ['Benign', 'Malignant']
predicted_class = class_labels[np.argmax(predictions_ct)]


# Print probabilities and predicted class
print(f"Probability of Benign: {probability_benign:.4f}")
print(f"Probability of Malignant: {probability_malignant:.4f}")
print(f"Predicted Class: {predicted_class}")
