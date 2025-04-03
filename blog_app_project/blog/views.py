from django.shortcuts import render
# from django.http import HttpResponse  # for using HttpResponse method
from .models import Post  # importing the Post model/table from the same package


# Create your views here.
def home(request):
    # data is passed into the template using the dictionary below
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context=context)


def about(request):
    # return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'blog/about.html', {'title': 'About'})  # returns http response
