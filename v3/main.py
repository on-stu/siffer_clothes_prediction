# 0. 사용할 패키지 불러오기
import numpy as np
import tensorflow as tf
import pandas as pd

# 1. 데이터셋 생성하기
data = pd.read_csv('../output.csv')
data = data[1:]
data = data.dropna()

yData = data['WeightOut']
xData = []

for i, rows in data.iterrows():
    xData.append([rows['POLYESTER'],rows['NYLON'],rows['POLYURETHANE'],rows['RAYON'],rows['POLYPROPYLENE'],rows['MODAL'],
            rows['POLYETHYLENE'],rows['COTTON'],rows['PTT'],rows['CUPRA'],rows['ACETATE'] ,rows['CORDURA'] ,rows['SILK'],rows['SPNDEX']])

print(yData, xData)

# 2. 모델 구성하기
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(64,  activation='relu'))
model.add(tf.keras.layers.Dense(64, activation='relu'))
model.add(tf.keras.layers.Dense(1))

# 3. 모델 학습과정 설정하기
model.compile(optimizer='rmsprop', loss='mse')

# 4. 모델 학습시키기
hist = model.fit(xData, yData, epochs=50)

# 5. 학습과정 살펴보기
# matplotlib inline
import matplotlib.pyplot as plt

plt.plot(hist.history['loss'])
plt.ylim(0.0, 1.5)
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train'], loc='upper left')
plt.show()

# 6. 모델 평가하기
loss = model.evaluate(xData, yData, batch_size=32)
print('loss : ' + str(loss))