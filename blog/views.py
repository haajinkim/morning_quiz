from django.shortcuts import render,redirect
from .models import Category,Article
# Create your views here.

def new_view(request):
    if request.method == 'POST':
        title = request.POST.get('title', None)
        content = request.POST.get('content', None)
        category_name = request.POST.get('category', None)
        category = Category.objects.get(name=category_name)
        article = Article.objects.create(title=title, content=content, category=category)
        return redirect('detail', article.pk)

    elif request.method == 'GET':
        categories = Category.objects.all()
        return render(request, 'new.html', {'categories':categories})

def category_view(request):
    categories = Category.objects.all()
    infos = {}
    for category in categories:
        infos[category.name] = Article.objects.filter(category=category).count()
    return render(request,'category.html', {'infos':infos})


def detail_view(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request,'detail.html',{'article':article})

def article_view(request, name):
    category = Category.objects.get(name=name)
    articles = Article.objects.filter(category=category)
    return render(request, 'article.html', {'articles': articles})
