from django.shortcuts import render
from . import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def index_page(req):
    pin_articles = models.Article.objects.filter(status=1, pin=1).order_by('-time')
    recent_articles = models.Article.objects.filter(status=1).order_by('-time')[:5]
    context = {
        'pin_articles': pin_articles,
        'recent_articles': recent_articles,
    }
    return render(req, 'blog/index.html', context=context)


def article_list(req):
    category = req.GET.get('category', None)
    tag = req.GET.get('tag', None)
    page = req.GET.get('page', '1')
    filter_string = ''
    if category:
        articles = models.Article.objects.filter(status=1, category=int(category)).order_by('-time')
        filter_string = 'category=' + category
    elif tag:
        articles = models.Article.objects.filter(status=1, tags=int(tag)).order_by('-time')
        filter_string = 'tag=' + tag
    else:
        articles = models.Article.objects.filter(status=1).order_by('-time')
    paginator = Paginator(articles, 10)  # 每页 10 篇文章
    try:
        ok_articles = paginator.page(int(page))
    except:
        ok_articles = paginator.page(1)
    context = {
        'articles': ok_articles,
        'filter_string': filter_string,
    }
    return render(req, 'blog/article_list.html', context=context)


def article_detail(req, article_id):
    article = models.Article.objects.filter(id=int(article_id))[0]
    context = {
        'article': article,
    }
    return render(req, 'blog/article_detail.html', context=context)


def category_list(req):
    categories = models.Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(req, 'blog/category_list.html', context=context)


def tag_list(req):
    tags = models.Tag.objects.all()
    context = {
        'tags': tags,
    }
    return render(req, 'blog/tag_list.html', context=context)


def about_page(req):
    return render(req, 'blog/about.html')