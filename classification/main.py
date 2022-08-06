import os
import pandas as pd
import tensorflow as tf
import numpy as np

data = pd.read_csv('../trainingData/woven.csv')
data = data[1:]
data = data.dropna()

yTemp = data['WeightOut'] #무게로 할지 두께로 할지
yData = []
for j, y in enumerate(yTemp):
    temp = []
    index = int(y) - 1
    for i in range(7):
        if(i == index):
            temp.append(1)
        else:
            temp.append(0)
    yData.append(temp)
xData = []

for i, rows in data.iterrows():
    xData.append([rows['POLYESTER'],rows['NYLON'],rows['POLYURETHANE'],rows['RAYON'],rows['POLYPROPYLENE'],rows['MODAL'],
            rows['POLYETHYLENE'],rows['COTTON'],rows['PTT'],rows['CUPRA'],rows['ACETATE'] ,rows['CORDURA'] ,rows['SILK'],rows['SPNDEX']])
# print(xData[0])
# trainX = xData[:40]
# trainY = yData[:40]
trainX = xData
trainY = yData

checkpoint_path = "training1/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)

cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path, save_weights_only=True, verbose=1)

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='relu'),   # input 개수가 아니라 Dense layer output 개수다.
    tf.keras.layers.Dense(256, activation='relu'),   # 숫자를 바꿔가면서 노드 개수와 hidden layer개수는 바꿔간다. 
    tf.keras.layers.Dense(7, activation='sigmoid')  # 1 - 7 수치 
])

# 보통 처음이 크고 가면서 작아진다
# 14 -> 64 -> 128 -> 256 -> 7

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
print(np.array(yData))

# latest = tf.train.latest_checkpoint(checkpoint_dir)
# model.load_weights(latest)

model.fit(np.array(trainX), np.array(trainY), epochs=1000, callbacks=[cp_callback])
# os.listdir(checkpoint_dir)
# model.save("saved_model/woven_weight")
# model.save("saved_model/woven_thick")

# predict
probability_model = tf.keras.Sequential([model, 
                                         tf.keras.layers.Softmax()])
predictions = probability_model.predict(np.array(xData[40: 50]))
# print(predictions[2])
print(np.argmax(predictions[3]), xData[42], yData[42])   
print(model.summary())                   

# predict = model.predict(np.array(xData) )
# print(np.argmax(predict[0]))

# new_model = tf.keras.models.load_model('saved_model/woven_weight')
# print(new_model.summary())

loss, acc = model.evaluate(trainX, trainY, verbose=2)
print('정확도: {:5.2f}%'.format(100*acc))