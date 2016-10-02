from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
class PostLV(ListView):
    model = Post
    context_object_name = 'post_list'


class PostDV(DetailView):
    model = Post
    context_object_name = 'post'
