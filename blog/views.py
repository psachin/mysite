from django.shortcuts import render
from models import Post


def post_list(request):
    posts = Post.objects.filter(published_date__isnull=False)
    posts = posts.order_by('published_date')
    query_dict = {
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', query_dict)

