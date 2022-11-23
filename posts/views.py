from django.shortcuts import render, redirect
from posts.models import Post, Comment, Hashtag
from posts.forms import PostCreateForm, CommentCreateForm


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
            'comments': comments,
            'form': CommentCreateForm
        }

        return render(request, 'posts/detail.html', context=data)

    if request.method == 'POST':
        form = CommentCreateForm(data=request.POST)

        if form.is_valid():
            Comment.objects.create(
                author_id=2,
                text=form.cleaned_data.get('text'),
                post_id=id
            )
            return redirect(f'/posts/{id}/')
        else:
            post = Post.objects.get(id=id)
            comments = Comment.objects.filter(post_id=id)

            data = {
                'post': post,
                'hashtags': post.hashtags.all(),
                'comments': comments,
                'form': form
            }

            return render(request, 'posts/detail.html', context=data)


def hashtags_view(request, **kwargs):
    if request.method == 'GET':
        hashtags = Hashtag.objects.all()

        data = {
            'hashtags': hashtags
        }

        return render(request, 'hashtags/hashtags.html', context=data)


def post_create_view(request):
    if request.method == 'GET':
        data = {
            'form': PostCreateForm
        }

        return render(request, 'posts/create.html', context=data)

    if request.method == 'POST':
        form = PostCreateForm(data=request.POST)

        if form.is_valid():
            Post.objects.create(
                author_id=1,
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description')
            )
            return redirect('/posts')
        else:
            data = {
                'form': form
            }
            return render(request, 'posts/create.html', context=data)
