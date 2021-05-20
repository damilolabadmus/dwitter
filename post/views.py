from django.shortcuts import redirect, render
from .models import Tweet
# Create your views here.

from post.forms import TweetForm


# def index(request):
#     all_tweets = TweetForm
#     context = {
#         "all_tweets": all_tweets
#     }
#     return render(request, 'post/index.html', context)


def index(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("post_index")
    else:
        all_tweets = Tweet.objects.all()
        tweet_form = TweetForm
        context = {
            "all_tweets": all_tweets, "tweet_form": tweet_form
        }
        return render(request, 'post/index.html', context)
