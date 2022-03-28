import json
import numpy as np
from textblob import TextBlob
from matplotlib import pyplot as plt

file = "collected_data_old/posts.json"
print(file)
values = []

with open(file) as f:
    data = json.load(f)
    print("Found ", len(data), " posts")
    for i in range(len(data)):
        try:
            blob = TextBlob(data[i]['message'])
            values.append([blob.sentiment.polarity, blob.sentiment.subjectivity])
        except:
            continue

val_array = np.asarray(values)
plt.scatter(val_array[:,1], val_array[:,0])
plt.axhline(y=0, color='black')
plt.xlabel("Subjectivity")
plt.ylabel("Polarity")
plt.show()