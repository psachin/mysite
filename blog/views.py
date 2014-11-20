from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse

# Local imports
from models import Post
from forms import PostForm


def post_list(request):
    """List all published posts ordered by published date.
    """
    posts = Post.objects.filter(published_date__isnull=False)
    posts = posts.order_by('published_date')
    query_dict = {
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', query_dict)


def post_details(request, pk):
    """Show the post.
    """
    post = get_object_or_404(Post, pk=pk)
    query_dict = {
        'post': post,
    }
    return render(request, 'blog/post_details.html', query_dict)


def post_new(request):
    """Publish new post.
    """
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            post.publish()
            return redirect('blog.views.post_details', pk=post.pk)
    else:
        form = PostForm()

    query_dict = {'form': form,}
    return render(request, 'blog/post_edit.html', query_dict)


def post_edit(request, pk):
    """Edit existing post.
    """
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            post.publish()
            return redirect('blog.views.post_details', pk=post.pk)
    else:
        form = PostForm(instance=post)

    query_dict = {'form': form,}
    return render(request, 'blog/post_edit.html', query_dict)

