from django.shortcuts import render
from .models import Post
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404


def create_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Post.objects.create(title=title, content=content)
        return redirect('show_posts')
    return render(request, 'blog/create_post.html')


def show_posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/show_posts.html', {'posts': posts})

def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('show_posts')

def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.save()
        return redirect('show_posts')
    return render(request, 'blog/edit_post.html', {'post': post})

