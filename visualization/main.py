import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../output.csv')
data = data[1:]
data = data.dropna()

labels = ["POLYESTER", "NYLON", "POLYURETHANE", "RAYON", "POLYPROPYLENE", "MODAL", "POLYETHYLENE", "COTTON", "PTT", "CUPRA", "ACETATE", "CORDURA", "SILK", "SPNDEX", "Weight", "Thick"]
values = {}
for label in labels:
    values[label] = []

for i, rows in data.iterrows():
    for label in labels:
        values[label].append(rows[label])

for i, label in enumerate(labels):
    plt.figure(i)
    plt.xlabel(label)
    plt.ylabel('Weight')
    plt.plot(values[label], values['Weight'], 'bo')
    
plt.show()
