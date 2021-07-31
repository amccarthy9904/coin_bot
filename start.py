import tensorflow as tf
from dataset import Dataset
from model import Model

data = Dataset()
data.load_data()
 
print(data.data_labels)
mod = Model()
