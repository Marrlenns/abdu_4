from django.urls import path
from posts.views import posts_view, detail_post_view

urlpatterns = [
    path('posts/', posts_view),
    path('posts/<int:id>/', detail_post_view)
]
