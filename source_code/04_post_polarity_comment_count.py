import json
from textblob import TextBlob
from matplotlib import pyplot as plt

file = "../Lab04_subjectivity_polarity/collected_data_old/posts.json"
print(file)
no_of_comments = []
post_values = []

with open(file) as f:
    data = json.load(f)
    print(len(data))
    for i in range(len(data)):
        post = data[i]
        try:
            post_text = post['message']
        except:
            continue

        blob = TextBlob(post_text)
        sentiment = []
        comment_file = "../Lab04_subjectivity_polarity/collected_data_old/{}_comments.json".format(data[i]['id'])
        comments = open(comment_file)
        comment_data = json.load(comments)
        post_values.append(blob.sentiment.polarity)
        no_of_comments.append(len(comment_data))

for i in range(100, 1000, 100):
    plt.plot(no_of_comments[i-100:i])
    plt.plot(post_values[i-100:i], color='r')
    plt.show()