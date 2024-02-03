from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Post


# Create your views here
def home(request):
    posts = Post.objects.all()[:10]
    #print(posts)
    data = {
        'posts':posts
    }
    return render(request,'home.html',data)
