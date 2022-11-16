from django.shortcuts import render
from posts.models import Post, Comment


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


def detail_post_view(request, id):
    if request.method == 'GET':
        post = Post.objects.get(id=id)
        comments = Comment.objects.filter(post_id=id)

        data = {
            'post': post,
            'hashtags': post.hashtags.all(),
            'comments': comments
        }

        return render(request, 'posts/detail.html', context=data)
