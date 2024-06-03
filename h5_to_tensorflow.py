import tensorflow as tf

model = tf.keras.models.load_model('my_model_new.h5')
tf.saved_model.save(model, '/tmp/my_saved_model')
