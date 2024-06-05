import tensorflow as tf
import os

# Suppress TensorFlow logging messages
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Load the Keras model
model = tf.keras.models.load_model('my_model.h5')

# Save the model in the TensorFlow SavedModel format
tf.saved_model.save(model, '/c/Users/awsli/kserve-tensorflow/saved_model')

print("Successfully saved the model as a TensorFlow SavedModel.")

