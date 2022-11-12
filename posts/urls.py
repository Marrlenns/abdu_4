from django.urls import path
from posts.views import posts_view

urlpatterns = [
    path('posts/', posts_view)
]
