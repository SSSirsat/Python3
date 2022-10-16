# -*- coding: utf-8 -*-
"""LSTM 24DEC2021.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fZZAMhdvGQZJvuxe3p9_K7z6qfHMwg8W
"""

import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import pandas_datareader as web
import datetime as dt
from sklearn.preprocessing import MinMaxScaler 

data = pd.read_csv('https://raw.githubusercontent.com/swapnilsaurav/Dataset/master/FB_Fin_Data.csv')
main_data = data
scaler = MinMaxScaler(feature_range=(0,1))
prediction_days = 60
data = scaler.fit_transform(data['Close'].values.reshape(-1,1))
X_train = []
y_train = []
for i in range(prediction_days, len(data)):
  X_train.append(data[i-prediction_days:i,0])
  y_train.append(data[i,0])

print(y_train)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM
import numpy as np
X_train, y_train = np.array(X_train), np.array(y_train)
X_train = np.reshape(X_train,(X_train.shape[0],X_train.shape[1],1))
def LSTM_Analysis():
  model = Sequential()
  model.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1],1)))
  model.add(Dropout(0.2))

  model.add(LSTM(units=50, return_sequences=True))
  model.add(Dropout(0.2))
  
  model.add(LSTM(units=50))
  model.add(Dropout(0.2))
  model.add(Dense(units=1))
  return model

md = LSTM_Analysis()
md.summary()
md.compile(optimizer='adam', loss='mean_squared_error')

from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
chkpointer = ModelCheckpoint(filepath='weights_best.hdf5', save_best_only = True)
md.fit(X_train, y_train, epochs=35, batch_size = 32, callbacks=[chkpointer])

# from google.colab import files
# upload_data = files.upload()
# test_data = upload_data

data2 = pd.read_csv('https://raw.githubusercontent.com/swapnilsaurav/Dataset/master/FB_Fin_Data.csv')
actual_values = data2['Close'].values
new_data = pd.concat((main_data['Close'],data2['Close']),axis=0)

X_test2 =[]
md_input = new_data[len(new_data) - len(data2)-prediction_days:].values
md_input = md_input.reshape(-1,1)
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0,1))

md_input = scaler.fit_transform(md_input)
for i in range(prediction_days, len(md_input)):
  X_test2.append(md_input[i-prediction_days:i,0])
#print(X_test2)

X_test2 = np.array(X_test2)
#print(X_test2.shape[1])
X_test2 = np.reshape(X_test2,(X_test2.shape[0], X_test2.shape[1],1))
#print(X_test2)
predicted_close = md.predict(X_test2)
predicted_close = scaler.inverse_transform(predicted_close)
print(predicted_close)

import matplotlib.pyplot as plt
plt.plot(actual_values, color="blue")
plt.plot(predicted_close, color="red")
plt.show()

