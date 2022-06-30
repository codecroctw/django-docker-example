from django.shortcuts import render
from .models import News

# Create your views here.


def home(req):
    latest_news = News.objects.all()
    return render(req, 'home.html', {
        'latest_news': latest_news,
    })
