from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from .models import *

def index(request):
    return render(request, "network/index.html", {
        "all_posts": Post.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")


@login_required(login_url='login')
def new_post(request):
    if request.method == 'POST':
        user = request.user
        content = request.POST['content']
        Post.objects.create(poster=user, content=content)


def profile(request, username):
    poster = get_object_or_404(User, username=username)

    poster_followers_count = poster.followers.count()
    poster_following_count = poster.following.count()
    poster_posts = poster.posts.order_by('-date')
    is_user_follow_him = poster in request.user.following.all()

    return render(request, "network/profile.html", {
    "poster": poster,
    "user_followers_count": poster_followers_count,
    "user_following_count": poster_following_count,
    "posts": poster_posts,
    "is_user_follow_him": is_user_follow_him
    })


def follow(request):
    if request.method == "POST":
        poster = User.objects.get(username=request.POST.get('poster'))
        follow = request.POST.get('follow') == 'follow'

        if follow:
            request.user.following.add(poster)
        else:
            request.user.following.remove(poster)
        return HttpResponseRedirect(reverse('profile', args=[poster]))


@login_required(login_url='login')
def following(request):
    following_posts = Post.objects.filter(poster__in=request.user.following.all())
    return render(request, "network/following.html", {
        "posts": following_posts,
    })


