from datetime import date
from collections import Counter
from django.shortcuts import render
from webapp.models import HackerNewsItem, HackerNewsItemSet


def home(request):
    latest_item_set = HackerNewsItemSet.objects.last()
    items = HackerNewsItem.objects.filter(item_set=latest_item_set)
    return render(request, 'main.html', {
        'items': items,
        'timestamp': latest_item_set and latest_item_set.timestamp
    })


def daily_summary(request):
    today = date.today()
    todays_items = HackerNewsItem.objects.filter(item_set__timestamp__startswith=today)
    # TODO: sort using both count and points
    top_30 = get_top_n_items(todays_items, 30)
    return render(request, 'main.html', {
        'items': sorted(top_30, key=lambda item: item.points, reverse=True),
        'timestamp': today
    })


def get_top_n_items(items, n):
    """
    Returns a list of the items with the highest frequency in items.
    """
    frequency_dict = get_frequency_dict(items)
    top_30 = sorted(frequency_dict.iteritems(), key=lambda item: item[1], reverse=True)[:n]
    return [item for item, _ in top_30]


def get_latest_item_by_url(url):
    return HackerNewsItem.objects.filter(url=url).last()


def get_frequency_dict(items):
    """
    Returns a dict containing pairs of (HackerNewsItem, frequency of item in items).
    """
    url_counts = Counter(it.url for it in items)
    return {get_latest_item_by_url(url): cnt for url, cnt in url_counts.items()}
