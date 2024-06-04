import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

model = tf.keras.models.load_model('my_model.h5')
tf.saved_model.save(model, '/tmp/my_saved_model')
