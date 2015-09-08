This app uses the [Scrapy framework](https://github.com/scrapy/scrapy) to gather information from the main page of Hacker News and uses Django to render the posts that were most relevant* in the current day.

* An item's relevance is defined as the number of ocurrences of the item throughout the datasets collected in the whole day.
