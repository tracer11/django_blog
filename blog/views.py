from django.shortcuts import render, redirect
from .models import Post
from .forms import PostCreation

def home(request):
  context = {
    'posts': Post.objects.all()
  }
  return render(request, 'blog/home.html', context)


def create(request):
  if request.method == 'POST':
    form = PostCreationForm(request.POST)
    if form.is_valid():
      form.save()
      redirect('')

  context = {'form' : form}

  return render(request, 'blog/create_post.html', context)


def about(request):
  return render(request, 'blog/about.html')


