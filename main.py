from keras.api.models import Sequential
from keras.api.layers import Dense
from keras.api.optimizers import SGD
from get_csv import getCsv


x,y = getCsv("altura_peso.csv")


modelo = Sequential()
modelo.add(Dense(x,y,activation='linear'))
sgd = SGD(lr=0.0004)

modelo.compile(loss='mse', optimizer=sgd)
modelo.summary()