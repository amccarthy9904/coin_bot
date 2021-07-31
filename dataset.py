import pandas as pd
import numpy as np
# Make numpy values easier to read.
np.set_printoptions(precision=3, suppress=True)

class Dataset:

    data_set = None
    data_labels = None
    input_path = 'data/BTC-USD_in.csv'

    def __init__(self) -> None:
        pass

    def load_data(self):
        data_frame = pd.read_csv(self.input_path, header=0)
        self.data_labels = np.array(data_frame.pop('Label'))
        self.data_set = np.array(data_frame)
        print(data_frame.head())
