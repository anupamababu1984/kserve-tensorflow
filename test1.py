!pip install tensorflow==2.13.1
!pip install keras==2.13.1

import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

# Path to the CT scan image
ct_image_path = "/content/nor3.jpg"

# Load the CT model
model_ct = load_model('/content/trained_modelweigtedattenCT.h5')

# Load CT scan image data
ct_scan_data = plt.imread(ct_image_path)

# Ensure the correct shape for the CT scan image data
ct_scan_data = image.img_to_array(ct_scan_data)
ct_scan_data = preprocess_input(ct_scan_data)
ct_scan_data = np.expand_dims(ct_scan_data, axis=0)  # Add batch dimension

# Make predictions using the CT model
predictions_ct = model_ct.predict(ct_scan_data)

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
