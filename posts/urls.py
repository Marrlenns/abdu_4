from django.urls import path
from posts.views import posts_view, detail_post_view, hashtags_view, post_create_view

urlpatterns = [
    path('posts/', posts_view),
    path('posts/<int:id>/', detail_post_view),
    path('hashtags/', hashtags_view),
    path('posts/create/', post_create_view)
]
