from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from .forms import PostCreationForm

class PostListView(ListView):
  model = Post
  template_name = 'blog/home.html'
  context_object_name = 'posts'
  ordering = ['-date_posted']

class PostDetailView(DetailView):
  model = Post






