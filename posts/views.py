from django.shortcuts import render, redirect
from posts.models import Post, Comment, Hashtag
from posts.forms import PostCreateForm, CommentCreateForm
from users.utils import get_user_from_request


# Create your views here.

PAGINATION_LIMIT = 4


def posts_view(request):
    if request.method == "GET":
        hashtag_id = request.GET.get('hashtag_id')
        search_text = request.GET.get('search')
        page = int(request.GET.get('page', 1))

        if hashtag_id:
            posts = Post.objects.filter(hashtags__in=[hashtag_id])
        else:
            posts = Post.objects.all()

        if search_text:
            posts = posts.filter(title__icontains=search_text)

        posts = [{
            'id': post.id,
            'title': post.title,
            'image': post.image,
            'description': post.description,
            'hashtags': post.hashtags.all()
        } for post in posts]

        max_page = round(posts.__len__() / PAGINATION_LIMIT)
        posts = posts[PAGINATION_LIMIT * (page-1):PAGINATION_LIMIT * page]

        data = {
            'posts': posts,
            'user': get_user_from_request(request),
            'hashtag_id': hashtag_id,
            'max_page': range(1, max_page+1)
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
            'form': CommentCreateForm,
            'user': get_user_from_request(request)
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
                'form': form,
                'user': get_user_from_request(request)
            }

            return render(request, 'posts/detail.html', context=data)


def hashtags_view(request, **kwargs):
    if request.method == 'GET':
        hashtags = Hashtag.objects.all()

        data = {
            'hashtags': hashtags,
            'user': get_user_from_request(request)
        }

        return render(request, 'hashtags/hashtags.html', context=data)


def post_create_view(request):
    if request.method == 'GET':
        data = {
            'form': PostCreateForm,
            'user': get_user_from_request(request)
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
                'form': form,
                'user': get_user_from_request(request)
            }
            return render(request, 'posts/create.html', context=data)
