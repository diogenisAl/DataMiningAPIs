import json
from textblob import TextBlob

file = "../Lab04_subjectivity_polarity/collected_data_old/posts.json"
print(file)
comment_values = []
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

        for j in range(len(comment_data)):
            blob_comment = TextBlob(comment_data[j]['message'])
            sentiment.append(blob_comment.sentiment.polarity)

        try:
            comment_values.append(sum(sentiment) / len(sentiment))
        except:
            comment_values.append(None)
        post_values.append(blob.sentiment.polarity)

post_pos = []
post_neg = []
post_neutral = []

post_pos_comment_pos = []
post_pos_comment_neg = []
post_pos_without_comments = []

post_neg_comment_neg = []
post_neg_comment_pos = []
post_neg_without_comments = []

for i in range(len(post_values)):

    if post_values[i] > 0:
        post_pos.append(post_values[i])
    elif post_values[i] < 0:
        post_neg.append(post_values[i])
    else:
        post_neutral.append(post_values[i])

    if comment_values[i] is None:
        if post_values[i] > 0:
            post_pos_without_comments.append([post_values[i], comment_values[i]])
        elif post_values[i] < 0:
            post_neg_without_comments.append([post_values[i], comment_values[i]])
        continue

    if post_values[i] > 0:
        if comment_values[i] >= 0:
            post_pos_comment_pos.append([post_values[i], comment_values[i]])
        else:
            post_pos_comment_neg.append([post_values[i], comment_values[i]])
    elif post_values[i] < 0:
        if comment_values[i] >= 0:
            post_neg_comment_pos.append([post_values[i], comment_values[i]])
        else:
            post_neg_comment_neg.append([post_values[i], comment_values[i]])

print("Percentage of positive posts: ", round(len(post_pos) / len(post_values) * 100, 2))
print("Percentage of negative posts: ", round(len(post_neg) / len(post_values) * 100, 2))
print("Percentage of neutral posts: ", round(len(post_neutral) / len(post_values) * 100, 2))
print("")
print("Percentage of positive posts with positive comments: ",
      round(len(post_pos_comment_pos) / len(post_pos) * 100, 2))
print("Percentage of positive posts with negative comments: ",
      round(len(post_pos_comment_neg) / len(post_pos) * 100, 2))
print("Percentage of positive posts without comments: ", round(len(post_pos_without_comments) / len(post_pos) * 100, 2))
print("")
print("Percentage of negative posts with positive comments: ",
      round(len(post_neg_comment_pos) / len(post_neg) * 100, 2))
print("Percentage of negative posts with negative comments: ",
      round(len(post_neg_comment_neg) / len(post_neg) * 100, 2))
print("Percentage of negative posts without comments: ", round(len(post_neg_without_comments) / len(post_neg) * 100, 2))