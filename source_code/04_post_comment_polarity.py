import json
from textblob import TextBlob
from matplotlib import pyplot as plt

file = "/collected_data_old/posts.json"
print(file)
comment_values = []
post_values = []

with open(file) as f:
    data = json.load(f)
    print(len(data))
    for i in range(len(data)):
        try:
            blob = TextBlob(data[i]['message'])
        except:
            continue

        sentiment = []
        comment_file = "../Lab04_subjectivity_polarity/collected_data_old/{}_comments.json".format(data[i]['id'])
        comments = open(comment_file)
        comment_data = json.load(comments)

        for j in range(len(comment_data)):
            blob_comment = TextBlob(comment_data[j]['message'])
            sentiment.append(blob_comment.sentiment.polarity)
        try:
            comment_values.append(sum(sentiment)/len(sentiment))
        except:
            comment_values.append(None)
        post_values.append(blob.sentiment.polarity)

plt.plot(post_values)
plt.plot(comment_values, 'r')
plt.show()
