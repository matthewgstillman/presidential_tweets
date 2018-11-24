from django.shortcuts import render
from tweet_dict import tweets
import requests
# from trump_tweets import tweets

import requests

# Create your views here.
def index(request):
    url = ("http://stash.compciv.org/2017/realdonaldtrump-tweets.json")
    response = requests.get(url)
    print("Response: {}".format(response))
    tweets = response.json()
    print("Tweets: {}".format(tweets))
    # contributors = tweets[0]
    # print("Contributors: {}".format(contributors))
    # print("Tweets: {}".format(tweets))
    context = {
        # 'contributors': contributors,
        'tweets': tweets,
    }
    return render(request, 'trump_tweets/index.html', context)