from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, 'mydiary/index.html', {'posts': posts})


