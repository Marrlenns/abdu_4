from django.shortcuts import render
from posts.models import Post


# Create your views here.

def posts_view(request):
    if request.method == "GET":
        posts = [{
            'id': post.id,
            'title': post.title,
            'image': post.image,
            'description': post.description,
            'hashtags': post.hashtags.all()
        } for post in Post.objects.all()]

        data = {
            'posts': posts
        }

        return render(request, 'posts/posts.html', context=data)
