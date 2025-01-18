import tensorflow as tf
import os

# Suppress TensorFlow logging messages
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Load the Keras model
model = tf.keras.models.load_model('4cls_DenseNet_without_cfr_with_Tuning.h5')

# Define the directory to save the model
save_dir = 'C:\\Users\\awsli\\kserve-tensorflow\\saved_model2\\2'

try:
    # Save the model in the TensorFlow SavedModel format
    tf.saved_model.save(model, save_dir)
    print("Successfully saved the model as a TensorFlow SavedModel.")
except Exception as e:
    print("An error occurred while saving the model:", e)


