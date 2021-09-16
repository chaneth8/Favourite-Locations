from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView 
from .models import Post, Users, Comment
from django import forms
from django.urls import reverse_lazy, reverse 
from django.http import HttpResponseRedirect, HttpResponse

def home(request, name):
    """Renders a list of all images and their titles""" 

    return render(request, "home.html", {
        "posts": Post.objects.all(),
        "name" : name,
    })

class login_form(forms.Form):    
    """Defines the two fields of the login page: the username, and the password""" 

    username = forms.CharField(max_length=100, label="Username")
    password = forms.CharField(max_length=100, label = "Password")

def login_screen(request):
    """Renders Login Page"""

    return render(request, 'login.html', {
        "form": login_form()
    })

def login(request):
    """Handles login - logs user if and only if there is no other user with the 
    inputted username, or his username and password matches an existing user."""

    if request.method == "POST":
        form = login_form(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            num_with_username = Users.objects.filter(username= username).count()
            num_username_and_password = Users.objects.filter(username= username, password= password).count()

            if num_with_username == 0 and num_username_and_password == 0:
                u = Users(username= username, password= password)
                u.save()
                return HttpResponseRedirect(reverse('home', args=[username]))
            
            elif num_with_username != 0 and num_username_and_password == 0:
                return render(request, 'login.html', {"form": login_form()})
            
            else:
                return HttpResponseRedirect(reverse('home', args=[username]))
    
        else:
            return render(request, 'login.html', {"form": login_form()})
    
    else:
        return render(request, 'login.html', {"form": login_form()})

def add_form(request, name):
    """Renders a form to allow user to add a new post"""

    return render(request, "add.html", {"name" : name})

def add(request, name):
    """Adds a new post based on data user inputted"""

    if request.method == 'POST':
        title = request.POST.get('title')
        location = request.POST.get('location')
        cover = request.FILES.get('cover')

        try: 
            p = Post(title=title, location=location, user=name, cover=cover)
            p.save()
            return HttpResponseRedirect(reverse('home', args=[name])) 
        
        except: 
            return HttpResponseRedirect(reverse('home', args=[name])) 

def delete_form (request, name):
    """Renders a form to allow user to delete a post"""

    user_posts = Post.objects.filter(user= name)

    return render(request, "delete.html", {
        "name": name,
        "user_posts": user_posts,
    })

def delete (request, name):
    """Renders the delete form, giving the user 
    the option to delete all posts posted by them."""

    if request.method == 'POST':
        post = request.POST.get('posts')
        user_posts = Post.objects.filter(title = post)
        user_posts.delete()

        post_comments = Comment.objects.filter(title = post)

        for post_comment in post_comments:
            post_comment.delete()

        return render(request, "home.html", {"posts": Post.objects.all(), "name" : name})

def add_comment_form (request, title, name):
    """Renders the add comment form"""

    return render(request, "add_comment_form.html", {"title": title, "name" : name})

def add_comment (request, title, name):
    """Adds the comment inputted by the user into the database"""

    if request.method == 'POST':
        comment = request.POST.get('comment')
        c = Comment(title=title, comment = comment)
        c.save()
        return HttpResponseRedirect(reverse('comments', args=[title, name])) 

def comments (request, title, name):
    """Renders a html page consisting of all comments on a post"""

    comments = Comment.objects.filter(title= title)
    return render(request, "comments.html", {"comments": comments, "name" : name})

def trip_planner(request, name):
    """Renders a html page allowing users to plan their trip"""

    return render(request, "tripplanner.html", {"name" : name})