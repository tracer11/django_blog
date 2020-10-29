from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UpdateUserForm, ProfileUpdateForm

# Create your views here.


def register(request):
  if request.method == 'POST':
    form = UserRegisterForm(request.POST)
    
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      messages.success(request, f'Welcome to the blog {username}!')
      return redirect('login')
  
  else:
    form = UserRegisterForm()
  
  return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
  if request.method == 'POST':
    update_user = UpdateUserForm(request.POST,instance = request.user)
    update_profile = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
    
    if update_user.is_valid() and update_profile.is_valid():
      update_user.save()
      update_profile.save()
      messages.success(request, 'Info updated succesfully!')
      return redirect('profile') 
  
  else:
    update_user = UpdateUserForm(instance = request.user)
    update_profile = ProfileUpdateForm(instance = request.user.profile)
  
  context = {
      'u_user': update_user,
      'u_profile': update_profile,
  }
  return render(request, 'users/profile.html', context)
