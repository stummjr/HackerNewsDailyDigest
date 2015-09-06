from datetime import datetime
from collections import defaultdict
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
    todays_item_sets = HackerNewsItemSet.objects.filter(
        timestamp__day=datetime.now().day,
        timestamp__month=datetime.now().month,
        timestamp__year=datetime.now().year
    )
    # TODO: improve this!!!
    items = []
    for item_set in todays_item_sets:
        items += list(HackerNewsItem.objects.filter(item_set=item_set))
    items_response = []
    for item, cnt in sorted(count(items).items(), key=lambda item: item[1], reverse=True)[:30]:
        items_response.append(HackerNewsItem.objects.filter(url=item)[0])
    return render(request, 'main.html', {
        'items': sorted(items_response,
                        key=lambda item: item.points and int(item.points.split(" ")[0]),
                        reverse=True),
        'timestamp': datetime.now().date()
    })


def count(items):
    d = defaultdict(int)
    for item in items:
        d[item.url] += 1
    return d
