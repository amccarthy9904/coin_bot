import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.layers.experimental import preprocessing
from tensorflow.python.ops.gen_array_ops import shape

class Model():

    mod = None

    def __init__(self) -> None:
        
        self.mod = tf.keras.Sequential()
        self.mod.add(tf.keras.Input(shape=(250,)))
        self.mod.add(layers.Dense)
        self.mod.compile()

