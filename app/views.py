from django.shortcuts import render

# Create your views here.

def Home(request):
  return render(request, 'main/index.html')

def Base(request):
  return render(request, 'main/base.html')

def About(request):
  return render(request, 'about.html')

def BlogSingle(request):
  return render(request, 'blog-single.html')

def Single(request):
  return render(request, 'blog-single-alt.html')

def Category(request):
  return render(request, 'category.html')

def Classic(request):
  return render(request, 'classic.html')

def Contact(request):
  return render(request, 'contact.html')

def Minimal(request):
  return render(request, 'minimal.html')

def Personal(request):
  return render(request, 'personal.html')
  
def PersonalAlt(request):
  return render(request, 'personal-alt.html')