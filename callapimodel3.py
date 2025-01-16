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
service_hostname = "tensorflow3.default.example.com"
ingress_host = "localhost"
ingress_port = "8080"
model_name = "tensorflow3"
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

# Get the class with the highest predicted probability
#predicted_class = np.argmax(predictions, axis=1)


# Optional: Print probabilities for each class
#class_labels = ['adeno', 'large', 'normal', 'squamous']  # Adjust based on your class labels
#for idx, label in enumerate(class_labels):
#   print(f"{label}: {predictions[0][idx]:.4f}")



# Get probabilities for each class
probability_adeno = predictions_ct[0][0]
probability_large = predictions_ct[0][1]
probability_normal = predictions_ct[0][2]
probability_squamous = predictions_ct[0][3]

# Determine the class with the highest probability
class_labels = ['adeno', 'large','normal','squamous']
predicted_class = class_labels[np.argmax(predictions_ct)]

# Print probabilities and predicted class
print(f"Probability of Adeno: {probability_adeno:.4f}")
print(f"Probability of Large: {probability_large:.4f}")
print(f"Probability of Normal: {probability_normal:.4f}")
print(f"Probability of Squamous: {probability_squamous:.4f}")
print(f"Predicted Class: {predicted_class}")

