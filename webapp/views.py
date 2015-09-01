from django.shortcuts import render
from webapp.models import HackerNewsItem


def home(request):
    items = HackerNewsItem.objects.all()
    return render(request, 'main.html', {'items': items})
