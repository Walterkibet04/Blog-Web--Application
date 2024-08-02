from django.shortcuts import render
from .models import Post, Category
# Create your views here.

def Home(request):
  popular_post = Post.objects.filter(section = 'Popular', status=1).order_by('-id')[0:4]
  recent_post = Post.objects.filter(section = 'Recent', status=1).order_by('-id')[0:4]
  main_post = Post.objects.filter(Main_post = True, status=1)[0:1]
  Editor_pick = Post.objects.filter(section = 'Editors_pick', status=1).order_by('-id')
  trending = Post.objects.filter(section = 'Trending', status=1).order_by('-id') 
  inspiration = Post.objects.filter(section = 'Inspiration', status=1).order_by('-id')[0:2]
  latest_post = Post.objects.filter(section = 'Latest_post', status=1).order_by('-id')[0:4]

  category = Category.objects.all()



  context =  {
    'popular_post': popular_post,
    'recent_post': recent_post,
    'main_post': main_post,
    'Editor_pick': Editor_pick,
    'trending': trending,
    'inspiration': inspiration,
    'latest_post': latest_post,
    'category': category,
  }
  return render(request, 'main/index.html', context)

def Base(request):
  return render(request, 'main/base.html')

def About(request):
  return render(request, 'about.html')

def BlogSingle(request):
  return render(request, 'blog-single.html')

def Single(request):
  return render(request, 'blog-single-alt.html')

def Contact(request):
  return render(request, 'contact.html')

