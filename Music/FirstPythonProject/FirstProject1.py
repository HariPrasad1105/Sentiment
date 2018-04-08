import tweepy
import json
from JsonLoading import Preprocess
import csv

consumer_key = '2SMhnJBFkNs3oMkgefrt9fo5K'
consumer_secret = '0Fd3AdUPPwqxnGlI2rHqBnW4gHfUcdexViesIOHVwOJKVrxl9d'

access_token = '3034757418-WEdirAPltKQKZHy4jgnYnaIYHAkr3ayjgjRHbGE'
access_token_secret = 'xYdH8B6zH932Aklm9LafRMOeSaxMhSH2pvd5NkrTPsNg5'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


class StreamListerner(tweepy.StreamListener):

    def __init__(self, max_, api=None):
        self.api = api
        self.n = 0
        self.m = max_
        print(self.m)

    def on_data(self, data):
        self.n += 1
        if self.n < self.m:
            all_data = json.loads(data)
            tweet = all_data["text"]
            print(tweet)
            with open("E:\Hackathon\HackathonProject\Music\FirstPythonProject\static\macbookpro.csv", "a", encoding='utf-8', newline='') as f:
                csv_writer = csv.writer(f)
                result = Preprocess(tweet)
                print(result)
                if result != "None":
                    csv_writer.writerow([result])
                print("Preprocessing {} tweet into json file".format(self.n))
                return True
        else:
            print("No of tweets displayed : {}".format(str(self.n)))
            return False

    def on_error(self, status_code):
        print(status_code)


class Sentiment:

    def __init__(self, keyword, no_tweets):
        self.keyword = keyword
        self.noTweets = no_tweets
        print(self.keyword, self.noTweets)
        stream = tweepy.Stream(auth, StreamListerner(self.noTweets))
        stream.filter(languages=["en"], track=[self.keyword])


# Preprocess("tweetsexample.json")
# for t in tweepy.Cursor(api.search,
#                      q='#BaahubaliMovie',
#                     count=10,
#                    ).items(100):
# print(t.text)

senti = Sentiment('IPhoneX', 100)
