from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
import json
from django.http import JsonResponse

from .models import *

posts_count_per_page = 2
def index(request, page_number=1):
    p = Paginator(Post.objects.all(), posts_count_per_page)
    current_page = p.page(page_number)
    return render(request, "network/index.html", {
        "current_page": current_page,
        "pages": p,
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
    return HttpResponseRedirect(reverse('index'))


def profile(request, username, page_number=1):
    poster = get_object_or_404(User, username=username)

    poster_followers_count = poster.followers.count()
    poster_following_count = poster.following.count()
    poster_posts = poster.posts.order_by('-date')
    p = Paginator(poster_posts, posts_count_per_page)
    current_page = p.page(page_number)
    is_user_follow_him = poster in request.user.following.all()

    return render(request, "network/profile.html", {
        "poster": poster,
        "user_followers_count": poster_followers_count,
        "user_following_count": poster_following_count,
        "current_page": current_page,
        "pages": p,
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
def following(request, page_number=1):
    following_posts = Post.objects.filter(poster__in=request.user.following.all())
    p = Paginator(following_posts, posts_count_per_page)
    current_page = p.page(page_number)
    return render(request, "network/following.html", {
        "current_page": current_page,
        "pages": p,
    })


@login_required(login_url="login")
def edit(request, post_id):
    if request.method == "GET":
        return render(request, "network/edit.html", {
            "content": get_object_or_404(Post, pk=post_id, poster=request.user),
            "post_id": post_id,
        })
    
    try:
        object = get_object_or_404(Post, pk=post_id, poster=request.user)
    except Exception:
        return JsonResponse({'error': 'Invalid post'}, status=404)
    
    content = json.loads(request.body).get("content")
    object.content = content
    object.save()

    return JsonResponse({'message': 'Edit operation accomplished successfully'}, status=200)