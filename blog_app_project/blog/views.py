from django.shortcuts import render
from django.http import HttpResponse

# dummy data (for now)
posts = [
    {
        'author': 'User 1',
        'title': 'Blog Post 1',
        'content': 'First post in the blog page',
        'date_posted': 'March 01, 2025'
    },
    {
        'author': 'User 2',
        'title': 'Blog Post 2',
        'content': 'Second post in the blog page',
        'date_posted': 'March 02, 2025'
    }
]


# Create your views here.
def home(request):
    # data is passed into the template using the dictionary below
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context=context)


def about(request):
    # return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'blog/about.html', {'title': 'About'})  # returns http response
