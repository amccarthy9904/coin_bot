import pandas as pd
import numpy as np

# Make numpy values easier to read.
np.set_printoptions(precision=3, suppress=True)

import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.layers.experimental import preprocessing



class Dataset:

    def __init__(self) -> None:
        pass

    def load_data(self):
        data_frame = pd.read_csv('data/BTC-USD.csv', names=['Open','High','Low','Close','Volume','Green'])
        print(data_frame.head())
        data_labels = data_frame.pop('Green')
