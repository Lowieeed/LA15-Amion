from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

def say_hello(request):
    return HttpResponse("Hello Django")

def say_hi(request):
    return render(request, 'hi.html', {'name': 'Amion, Lhouei Jay P.'})

def blog_list(request):
    posts = Post.objects.all()  
    return render(request, 'blog_list.html', {'posts': posts})

def blog_detail(request, id):
    post = get_object_or_404(Post, id=id)  
    return render(request, 'blog_detail.html', {'post': post})