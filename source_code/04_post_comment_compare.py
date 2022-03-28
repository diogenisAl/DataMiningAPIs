import json
from textblob import TextBlob
from matplotlib import pyplot as plt

file = "../Lab04_subjectivity_polarity/collected_data_old/posts.json"
id = input("Please provide an id: ")
with open(file) as f:
    data = json.load(f)
    blob_post = None
    for i in range(len(data)):
        if data[i]['id'] == id:
            blob_post = TextBlob(data[i]['message'])
            print(data[i]['message'])

    if blob_post == None:
        print("No post found")
#         exit()

    sentiment = []
    comment_file = "../Lab04_subjectivity_polarity/collected_data_old/{}_comments.json".format(id)
    comments = open(comment_file)
    comment_data = json.load(comments)
    if len(comment_data) > 0:
        print(len(comment_data))
        for j in range(len(comment_data)):
            blob_comment = TextBlob(comment_data[j]['message'])
            sentiment.append(blob_comment.sentiment.polarity)
        plt.bar(["Post Polarity", "Comment avg Polarity"], [blob_post.sentiment.polarity, sum(sentiment)/len(sentiment)])
        plt.axhline(y=0, color='black')
        plt.show()
        print(blob_post.sentiment.polarity, sum(sentiment)/len(sentiment))