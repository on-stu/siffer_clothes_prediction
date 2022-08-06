import tensorflow as tf
import numpy as np


new_model = tf.keras.models.load_model('saved_model/woven_weight')

vals = [0.0,86.0,14.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
# exit()
output = new_model.predict(np.array(vals).reshape((1, -1)))
print(np.argmax(output[0]) + 1)
