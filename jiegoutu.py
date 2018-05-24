#coding:utf-8
from keras.models import Sequential
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import AveragePooling2D,MaxPooling2D
# from keras.layers.core import Activation
# from keras.layers.core import Flatten
from keras.layers.core import Dense
from keras.layers import Dropout, Flatten,LeakyReLU
from keras import backend as K
from keras.layers import Input, Convolution2D, Flatten, Dense, Activation
from keras.models import Sequential
from keras.optimizers import SGD , Adam
from keras import initializers

from keras.utils.vis_utils import plot_model

from keras import Sequential
from keras.layers import LSTM, Dense
#from data_note import scaler, test_x, train_X, test_X, train_y, test_y
import matplotlib.pyplot as plt
from numpy import concatenate  # 数组拼接
from math import sqrt
from sklearn.metrics import mean_squared_error
#from model.pred import MAPE,eva_regress



model = Sequential()



model.add(LSTM(50, input_shape=(20000, 6)))
model.add(Dense(1))


plot_model(model, to_file='structure.png', show_shapes=True)
