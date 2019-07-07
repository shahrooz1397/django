from django.shortcuts import render
from .models import Post

# Create your views here.

def index(request):
    domy = {'posts':Post.objects.all()}
    return render(request, 'blog/index.html', domy)



def about(request):
    return render(request, 'blog/about.html')
