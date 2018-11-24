from django.shortcuts import render
from tweet_dict import *
import requests
# from trump_tweets import tweets

import requests

# Create your views here.
def index(request):
    # tweets = tweet_dict
    # print("Tweets: {}".format(tweets))
    url = ("http://stash.compciv.org/2017/realdonaldtrump-tweets.json")
    response = requests.get(url)
    tweets = response.json()
    for i in range(0, len(tweets)):
        contributors = tweets[i]['contributors']
        print("Contributors: {}".format(contributors))
        tweet_text = tweets[i]['text']
        # print("Tweet Text: {}".format(tweet_text))
    context = {
        'contributors': contributors,
        'tweets': tweets,
    }
    return render(request, 'trump_tweets/index.html', context)