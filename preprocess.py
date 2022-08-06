import csv

dataPath = 'clothes.csv'
outputPath = 'output.csv'
outputOpen = open(outputPath, 'w')

columns = ['Fabric','ProductName','POLYESTER','NYLON','POLYURETHANE','RAYON','POLYPROPYLENE','MODAL',
            'POLYETHYLENE','COTTON','PTT' ,'CUPRA','ACETATE' ,'CORDURA' ,'SILK','SPNDEX','Weight','Thick','WeightOut',
            'ThickOut']
csvData = []
fileOpen = open(dataPath, 'r', encoding='utf-8-sig')
fileRead = csv.DictReader(fileOpen)
tempDict ={}

def getWeightOut( fabric, weight):
    if(fabric == "woven"):
        if(weight < 12.6):
            return 1
        elif(weight < 16.6):
            return 2
        elif(weight < 20.6):
            return 3
        elif(weight < 24.6):
            return 4
        elif(weight < 28.6):
            return 5
        elif(weight < 32.6):
            return 6
        else:
            return 7
    elif(fabric == "knit"):
        if(weight < 5.85):
            return 1
        elif(weight < 8.32):
            return 2
        elif(weight < 10.79):
            return 3
        elif(weight < 13.26):
            return 4
        elif(weight < 15.73):
            return 5
        elif(weight < 18.2):
            return 6
        else:
            return 7
    else:
        return 0


def getThickOut(fabric, thick):
    if(fabric == "woven"):
        if(thick < 0.48):
            return 1
        elif(thick < 0.62):
            return 2
        elif(thick < 0.76):
            return 3
        elif(thick < 0.9):
            return 4
        elif(thick < 1.04):
            return 5
        elif(thick < 1.18):
            return 6
        else:
            return 7
    elif(fabric == 'knit'):
        if(thick < 0.065):
            return 1
        elif(thick < 0.12):
            return 2
        elif(thick < 0.19):
            return 3
        elif(thick < 0.26):
            return 4
        elif(thick < 0.33):
            return 5
        elif(thick < 0.4):
            return 6
        else:
            return 7
    else:
        return 0


for rows in fileRead:
    csvData.append(rows)

for i, col in enumerate(columns):
    outputOpen.write(col)
    if(i < len(columns) - 1):
        outputOpen.write(',')
    else:
        outputOpen.write('\n')

for rows in csvData:
    for i, col in enumerate(columns):
        if(col == 'Usage'):
            outputOpen.write("\"{}\"".format(rows[col]))
        elif(col=='WeightOut'):
            fabric = rows['Fabric']
            weight = rows['Weight']
            if(weight == ""):
                weight = 0
            weight = float(weight)
            weightOut = getWeightOut(fabric, weight)
            weightOut = str(weightOut)
            outputOpen.write(weightOut)
        elif(col=='ThickOut'):
            fabric = rows['Fabric']
            thick = rows['Thick']
            if(thick == ""):
                thick = 0
            thick = float(thick)
            thickOut = getThickOut(fabric, thick)
            thickOut = str(thickOut)
            outputOpen.write(thickOut)
        else:
            if(col == "Fabric" or col == "ProductName"):
                outputOpen.write(rows[col])
            else:
                value = rows[col]
                if(value == ""):
                    value = 0
                value = float(value)
                outputOpen.write(str(value))
        if(i < len(columns) - 1):
            outputOpen.write(',')
        else:
            outputOpen.write('\n')


