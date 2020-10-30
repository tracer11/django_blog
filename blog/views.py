from django.shortcuts import render
from django.views.generic import (ListView, DetailView, CreateView, UpdateView)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post

class PostListView(ListView):
  model = Post
  template_name = 'blog/home.html'
  context_object_name = 'posts'
  ordering = ['-date_posted']

class PostDetailView(DetailView):
  model = Post
  template_name = 'blog/detail.html'

class PostCreateView(LoginRequiredMixin,  CreateView): 
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
      form.instance.author = self.request.user
      return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
      form.instance.author = self.request.user
      return super().form_valid(form)







