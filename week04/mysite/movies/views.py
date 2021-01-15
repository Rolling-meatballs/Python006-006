from django.shortcuts import render
from spider.spider import spider


# Create your views here.

def index(request):
    items = spider()
    return render(request, 'movies/index.html', {'items': items})
