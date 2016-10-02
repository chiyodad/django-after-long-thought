from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
class PostLV(ListView):
    model = Post
    context_object_name = 'post_list'

"""
class PostDV(DetailView):
    model = Post
    context_object_name = 'post'
"""

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})
