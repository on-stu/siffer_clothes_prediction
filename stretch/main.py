import pandas as pd
import tensorflow as tf
import numpy as np

data = pd.read_csv('preprocessed.csv')
data = data.dropna()

xData = []
# yData = data['LastStretchForce']
yData = data['LastStretchLength']
for i, rows in data.iterrows():
    xData.append([rows['POLYESTER'],rows['NYLON'],rows['POLYURETHANE'],rows['RAYON'],rows['POLYPROPYLENE'],rows['MODAL'],
            rows['POLYETHYLENE'],rows['COTTON'],rows['PTT'],rows['CUPRA'],rows['ACETATE'] ,rows['CORDURA'] ,rows['SILK'],rows['SPNDEX']])
    # yData.append([data['LastStretchForce'],data['LastStretchLength']])

trainX = list(xData)
trainY = list(yData)


# print(trainX[0], trainY[0])
# exit()

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='relu'),   # input 개수가 아니라 Dense layer output 개수다.
    tf.keras.layers.Dense(256, activation='relu'),   # 숫자를 바꿔가면서 노드 개수와 hidden layer개수는 바꿔간다. 
    tf.keras.layers.Dense(256, activation='relu'), 
    tf.keras.layers.Dense(256, activation='relu'), 
    tf.keras.layers.Dense(256, activation='relu'), 
    tf.keras.layers.Dense(256, activation='relu'), 
    tf.keras.layers.Dense(1)
])

# 보통 처음이 크고 가면서 작아진다
# 14 -> 64 -> 128 -> 256 -> 7

# model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.compile(optimizer='adam', loss='mse', metrics=['mse', 'accuracy'])


model.fit(np.array(trainX), np.array(trainY), epochs=1000)             
print(model.summary())

predict = model.predict(np.array(trainX) )
print('prediction:' ,predict[1], trainY[1])
