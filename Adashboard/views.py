from django.shortcuts import render, redirect
from users.models import Profile
from blog.models import *
from django.contrib.auth.models import User
from blog.forms import *


# Create your views here.
def dashboard(request):
    blog_count = Post.objects.all().count()
    user_count = User.objects.all().count()
    context = {
        'blog_count': blog_count,
        'user_count': user_count
    }
    return render(request, 'Adashboard/admin_dash.html', context)


def show_users(request):
    users = User.objects.all()
    context = {
        "users": users,
    }
    return render(request, 'Adashboard/admin_user.html', context)


def show_post(request):
    users = Profile.objects.all()
    posts = Post.objects.all()
    context = {
        "users": users,
        'posts': posts,
        'form': Form
    }
    return render(request, 'Adashboard/admin_post.html', context)


def delete_post(request, p_id):
    posts = Post.objects.get(id=p_id)
    posts.delete()
    return redirect("posts")

