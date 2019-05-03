import tweepy
from textblob import TextBlob
from matplotlib import pyplot


ConsumerKey="0AMCsJCHiiVN4poE0YZBuIh1i"
ConsumerSecret="J7PIJcaFOFCd7e3POYWS5HY8KbP7EV1pa91XqcgY0a3GVAVgu7"
AccessToken = "959518738604179456-bFtcKdEfZJMejepZJkI0PXNMBtTcYWb"
AccessTokenSecret = "THKXlzYZ6vWIgxNFDvo4RRPKW83m63MfsfFEx91nka9n2"


Authentication = tweepy.OAuthHandler(ConsumerKey, ConsumerSecret)
Authentication.set_access_token(AccessToken, AccessTokenSecret)

tweety = tweepy.API(Authentication)

tweets = tweety.search(q="Bitcoin", count=1, result_type = "recent")

sentiment = []
dates = ["2018-02-05", "2018-02-06", "2018-02-07", "2018-02-08", "2018-02-09", "2018-02-10", "2018-02-11"]
avgSentiment = []
for i in range(7):
    tweets = tweety.search(q="bitcoin", count=100, until=dates[i], result_type = "recent")
    for tweet in tweets:
        sentimenty = TextBlob(tweet.text)
        if sentimenty.sentiment[0] != 0:
            sentiment.append(sentimenty.sentiment[0])

print("Number of Data Points: " + str(len(sentiment)))
print("Average Value of Sentiment: " + str(sum(sentiment)/len(sentiment)))
pyplot.hist(sentiment, rwidth=0.5)
pyplot.show()






