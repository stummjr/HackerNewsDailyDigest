import scrapy
from w3lib import url
from urlparse import urljoin
from datetime import datetime
from webapp.models import HackerNewsItemSet
from scrapy.linkextractors import LinkExtractor
from crawler.hackernews.items import HackerNewsItem, CommentItem


class HackerNewsSpider(scrapy.Spider):
    name = "hnews"
    allowed_domains = ["ycombinator.com"]
    start_urls = ["http://news.ycombinator.com"]

    def __init__(self, pages_to_follow=0, *args, **kwargs):
        super(HackerNewsSpider, self).__init__(*args, **kwargs)
        self.pages_to_follow = int(pages_to_follow)

    def parse(self, response):
        item_set = HackerNewsItemSet()
        item_set.timestamp = datetime.now()
        item_set.save()
        for sel in response.xpath("//tr[@class='athing']"):
            item = self.extract_news_item(sel, item_set, response)
            yield item
            # ads have no comments
            # if 'comments_url' in item and item['comments_url'] is not None:
            #     yield scrapy.Request(
            #         item['comments_url'], callback=self.parse_comments
            #     )
        next_page = LinkExtractor(restrict_xpaths="//a[string(.)='More']").extract_links(response)
        if next_page and self.pages_to_follow:
            self.pages_to_follow -= 1
            yield scrapy.Request(next_page[-1].url, callback=self.parse)

    def parse_comments(self, response):
        items = []
        # the first item is not a comment
        for athing_sel in response.xpath('//tr[@class="athing"]')[1:]:
            comment_item = CommentItem()
            hacker_news_item = url.url_query_parameter(response.url, "id")
            add_if_not_none(comment_item, 'hacker_news_item', hacker_news_item)
            nesting_level = int(
                athing_sel.xpath(".//td[@class='ind']/img/@width").extract_first()
            )
            add_if_not_none(comment_item, 'nesting_level', nesting_level)
            text = "\n".join(
                athing_sel.xpath(
                    ".//td[@class='default']//span[@class='comment']//text()"
                ).extract()[1:-6]
            )
            add_if_not_none(comment_item, 'text', text)
            user_name = athing_sel.xpath(
                ".//td[@class='default']//span[@class='comhead']/"
                "a[starts-with(@href, 'user')]/text()"
            ).extract_first()
            add_if_not_none(comment_item, 'user_name', user_name)
            comment_id = athing_sel.xpath(
                ".//td[@class='default']//a[starts-with(@href, 'item')]/@href"
            ).extract_first()
            add_if_not_none(comment_item, 'comment_id', comment_id)
            comment_item['hacker_news_item'] = response.url
            items.append(comment_item)
        self.fill_parents(items)
        for item in items:
            yield item

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
        add_if_not_none(news_item, 'points', points)
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
        add_if_not_none(news_item, 'comments', comments)
        comments_path = details_sel.xpath("./a[starts-with(@href, 'item')]/@href").extract_first()
        comments_url = (comments_path and urljoin(response.url, comments_path))
        add_if_not_none(news_item, 'comments_url', comments_url)
        return news_item

    def get_parent_of(self, comments, cur):
        for i in range(cur, -1, -1):
            if comments[i]['nesting_level'] < comments[cur]['nesting_level']:
                return comments[i]['comment_id'] if 'comment_id' in comments[i] else None

    def fill_parents(self, comments):
        for i, item in enumerate(comments):
            item['parent'] = self.get_parent_of(comments, i)


def add_if_not_none(dict_item, key, value):
    if value is not None:
        dict_item[key] = value
