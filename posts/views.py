from django.shortcuts import render
from posts.models import Post, Comment, Hashtag


# Create your views here.

def posts_view(request):
    if request.method == "GET":
        hashtag_id = request.GET.get('hashtag_id')

        if hashtag_id:
            posts = Post.objects.filter(hashtags__in=[hashtag_id])
        else:
            posts = Post.objects.all()

        posts = [{
            'id': post.id,
            'title': post.title,
            'image': post.image,
            'description': post.description,
            'hashtags': post.hashtags.all()
        } for post in posts]

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


def hashtags_view(request, **kwargs):
    if request.method == 'GET':
        hashtags = Hashtag.objects.all()

        data = {
            'hashtags': hashtags
        }

        return render(request, 'hashtags/hashtags.html', context=data)