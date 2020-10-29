from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

class PostListView(ListView):
  model = Post
  template_name = 'blog/home.html'
  context_object_name = 'posts'
  ordering = ['-date_posted']

class PostDetailView(DetailView):
  model = Post
  template_name = 'blog/detail.html'

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']









