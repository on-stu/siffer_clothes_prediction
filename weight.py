import tensorflow as tf
import pandas as pd

data = pd.read_csv('trainingData/woven.csv')
data = data[1:]
data = data.dropna()

# print(data)
# yTemp = data['WeightOut'] #무게로 할지 두께로 할지
yTemp = data['ThickOut']

yData = []
for j, y in enumerate(yTemp):
    temp = []
    index = int(y) - 1
    # print(y, index, j)
    for i in range(7):
        if(i == index):
            temp.append(1)
        else:
            temp.append(0)
    yData.append(temp)
# print(yData)
# exit()
# yData = data['ThickOut']

xData = []

for i, rows in data.iterrows():
    xData.append([rows['POLYESTER'],rows['NYLON'],rows['POLYURETHANE'],rows['RAYON'],rows['POLYPROPYLENE'],rows['MODAL'],
            rows['POLYETHYLENE'],rows['COTTON'],rows['PTT'],rows['CUPRA'],rows['ACETATE'] ,rows['CORDURA'] ,rows['SILK'],rows['SPNDEX']])
# print(xData[0])
trainX = xData
trainY = yData

# new_model = tf.keras.models.load_model('saved_model/woven_weight')
new_model = tf.keras.models.load_model('saved_model/woven_thick')
print(new_model.summary())

loss, acc = new_model.evaluate(trainX, trainY, verbose=2)
print('정확도: {:5.2f}%'.format(100*acc))