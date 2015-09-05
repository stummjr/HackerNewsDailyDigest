from django.shortcuts import render
from webapp.models import HackerNewsItem, HackerNewsItemSet


def home(request):
    latest_item_set = HackerNewsItemSet.objects.last()
    items = HackerNewsItem.objects.filter(item_set=latest_item_set)
    return render(request, 'main.html', {'items': items, 'timestamp': latest_item_set.timestamp})
