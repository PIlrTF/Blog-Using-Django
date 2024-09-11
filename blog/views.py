# blog/views.py

from django.http import HttpResponseRedirect
from django.shortcuts import render
from blog.models import Post, Comment
from blog.forms import CommentForm

# ...
def blog_index(request):
    posts = Post.objects.all().order_by("-date_created")
    context = {
        "posts": posts,
    }
    return render(request, "blog/index.html", context)
def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by("-date_created")
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "blog/category.html", context)
'''def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
    }

    return render(request, "blog/detail.html", context)'''
def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(request.path_info)

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    return render(request, "blog/detail.html", context)