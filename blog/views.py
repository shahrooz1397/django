from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from django.views.generic import (
        ListView,
        DetailView,
        UpdateView,
        CreateView)

# Create your views here.

def index(request):
    domy = {'posts':Post.objects.all()}
    return render(request, 'blog/index.html', domy)


class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'#<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def about(request):
    return render(request, 'blog/about.html')
