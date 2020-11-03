from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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

    #automaitcally adds current user as post author
    def form_valid(self, form):
      form.instance.author = self.request.user
      return super().form_valid(form)

class PostUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    
    #tests to see if current user is the post author
    def test_func(self):
      post = self.get_object()
      if self.request.user == post.author:
        return True 
      else:
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post

    success_url = reverse_lazy('blog-home')

    def test_func(self):
      post = self.get_object()
      if self.request.user == post.author:
        return True
      else:
        return False







