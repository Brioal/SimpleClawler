# encoding=utf-8
class UrlManager(object):
    def __init__(self):
        self.new_urls = []
        self.old_urls = []

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.append(url)

    def add_new_urls(self, urls):
        if urls is None:
            return
        if len(urls) == 0:
            return
        for url in urls:
            self.new_urls.append(url)

    def has_news_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        new_url = self.new_urls.pop(0)
        self.old_urls.append(new_url)
        return new_url
