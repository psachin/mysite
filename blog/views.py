from django.shortcuts import render, get_object_or_404

# Local imports
from models import Post


def post_list(request):
    posts = Post.objects.filter(published_date__isnull=False)
    posts = posts.order_by('published_date')
    query_dict = {
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', query_dict)


def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    query_dict = {
        'post': post,
    }
    return render(request, 'blog/post_details.html', query_dict)
