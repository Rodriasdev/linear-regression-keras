from keras.api.models import Sequential
from keras.api.layers import Dense
from keras.api.optimizers import SGD
import matplotlib.pyplot as plt
import numpy as np
from get_csv import getCsv


x, y = getCsv("altura_peso.csv")


modelo = Sequential()
input_dim = 1
output_dim = 1
modelo.add(Dense(output_dim, input_dim=input_dim, activation='linear'))


sgd = SGD(learning_rate=0.0004, clipvalue=1.0)

modelo.compile(loss='mse', optimizer=sgd)


modelo.summary()


num_epochs = 10000
batch_size = x.shape[0]
historia = modelo.fit(x, y, epochs=num_epochs, batch_size=batch_size,
verbose=1)

capas = modelo.layers[0]  
w, b = capas.get_weights() 
print('Parámetros: w = {:.1f}, b = {:.1f}'.format(w[0][0], b[0]))

plt.subplot(1,2,1)
plt.plot(historia.history['loss'])
plt.xlabel('epoch')
plt.ylabel('ECM')
plt.title('ECM vs. epochs')
y_regr = modelo.predict(x)
plt.subplot(1, 2, 2)
plt.scatter(x,y)
plt.plot(x,y_regr,'r')
plt.title('Datos originales y regresión lineal')
plt.show()


x_pred = np.array([170])
y_pred = modelo.predict(x_pred)
print("El peso será de {:.1f} kg".format(y_pred[0][0]), 
      "para una persona que mide {} cm".format(x_pred[0]))