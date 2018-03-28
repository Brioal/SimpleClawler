# encoding=utf-8
import url_manager
import url_download
import url_paraser
import url_out



url_main = "https://baike.baidu.com/item/Python/407313"
# url_main = "http://python.org"


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = url_download.Downloader()
        self.paraser = url_paraser.Parser()
        self.outer = url_out.Ouputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_news_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d " %s' % (count, new_url)
                html_content = self.downloader.download(new_url)
                new_urls, new_data = self.paraser.parase(new_url, html_content)
                self.urls.add_new_urls(new_urls)
                self.outer.collect_data(new_data)
                if count == 100:
                    break
                count += 1
            except:
                print "craw Failed"
        self.outer.out_put_html()


if __name__ == "__main__":
    root_url = url_main
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
