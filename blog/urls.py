from django.urls import path
from . import views 
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='blog-detail'),
    path('create/', PostCreateView.as_view(), name='blog-create'),
    path('update/<int:pk>', PostUpdateView.as_view(), name='blog-update'),
]


