import scrapy
from urlparse import urljoin
from webapp.models import HackerNewsItemSet
from scrapy.linkextractors import LinkExtractor
from crawler.hackernews.items import HackerNewsItem


class HackerNewsSpider(scrapy.Spider):
    name = "hnews"
    allowed_domains = ["ycombinator.com"]
    start_urls = ["http://news.ycombinator.com"]

    def __init__(self, pages_to_follow=0, *args, **kwargs):
        super(HackerNewsSpider, self).__init__(*args, **kwargs)
        self.pages_to_follow = int(pages_to_follow)

    def parse(self, response):
        item_set = HackerNewsItemSet()
        item_set.save()
        for sel in response.xpath("//tr[@class='athing']"):
            item = self.extract_news_item(sel, item_set, response)
            yield item
        next_page = LinkExtractor(restrict_xpaths="//a[string(.)='More']").extract_links(response)
        if next_page and self.pages_to_follow:
            self.pages_to_follow -= 1
            yield scrapy.Request(next_page[-1].url, callback=self.parse)

    def extract_news_item(self, sel, item_set, response):
        news_item = HackerNewsItem()
        news_item['item_set'] = item_set
        link_sel = sel.xpath("./td[@class='title']")
        title = link_sel.xpath("./a/text()").extract_first()
        add_if_not_none(news_item, 'title', title)
        url = link_sel.xpath("./a/@href").extract_first()
        add_if_not_none(news_item, 'url', url)
        details_sel = sel.xpath("./following-sibling::*[position()=1]/td[@class='subtext']")
        points = details_sel.xpath("./span[@class='score']/text()").extract_first()
        add_if_not_none(news_item, 'points', 0 if not points else int(points.split(" ")[0]))
        user_name = details_sel.xpath(
            "./a[starts-with(@href, 'user')]/text()"
        ).extract_first()
        add_if_not_none(news_item, 'user_name', user_name)
        since = details_sel.xpath(
            "./a[starts-with(@href, 'item')][contains(., 'ago')]/text()"
        ).extract_first()
        add_if_not_none(news_item, 'since', since)
        comments = details_sel.xpath(
            "./a[starts-with(@href, 'item')][contains(., 'comment') or"
            "contains(., 'discuss')]/text()"
        ).extract_first()
        comments = 0 if not comments or comments == "discuss" else int(comments.split(" ")[0])
        add_if_not_none(news_item, 'comments', comments)
        comments_path = details_sel.xpath("./a[starts-with(@href, 'item')]/@href").extract_first()
        comments_url = (comments_path and urljoin(response.url, comments_path))
        add_if_not_none(news_item, 'comments_url', comments_url)
        return news_item


def add_if_not_none(dict_item, key, value):
    if value is not None:
        dict_item[key] = value
