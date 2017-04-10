from django.shortcuts import render, get_object_or_404
from .models import SavedUser, Tweets
from . import tweet_profiler
from .forms import HandleForm, PushForm


def index(request):
    context = {}
    return render(request, 'profileGrabber/index.html', context)


def discover(request):
    profile = tweet_profiler.get_profile ("realDonaldTrump")
    influencer = "NO"

    if request.method == 'POST':
        render_handle = HandleForm(request.POST)
        render_push = PushForm(request.POST)

        if render_handle.is_valid():
            profile = tweet_profiler.get_profile(render_handle.cleaned_data['twitter_handle'])
            render_push = PushForm()

        elif render_push.is_valid():
            profile = tweet_profiler.get_profile(render_push.cleaned_data['push_handle'])
            tweets = tweet_profiler.get_tweets(render_push.cleaned_data['push_handle'])

            try:
                s = SavedUser(
                    source = render_push.cleaned_data['push_source'],
                    handle = profile.screen_name,
                    name = profile.name,
                    followers = profile.followers_count,
                    following = profile.friends_count,
                    influencer = influencer,
                    description = profile.description
                    )
                s.save()

                for tweet in tweets:
                    t = Tweets(
                        user_name = s, 
                        tweet_text = tweet.text
                        )
                    t.save()
            
            except:
                s = ""
                render_handle = HandleForm() 

        else:
            render_handle = HandleForm()
            render_push = PushForm()
    
    if profile.followers_count > 500:
        influencer = "YES"

    context = {
    'profile': profile,
    'influencer': influencer,
    }
    return render(request, 'profileGrabber/discover.html', context)


def collection(request):
    saved_users = SavedUser.objects.all()
    tweets = Tweets.objects.all()
    context = {
    'saved_users': saved_users,
    'tweets': tweets,
    }
    return render(request, 'profileGrabber/collection.html', context)
