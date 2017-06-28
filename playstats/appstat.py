from urllib.request import urlopen
from lxml import html
from lxml.cssselect import CSSSelector


class AppStat:
    def __init__(self, package_name):
        self.app_url = "https://play.google.com/store/apps/details?id=%s" % package_name

    def get_rating(self):
        content = urlopen(self.app_url).read()
        tree = html.fromstring(content)
        selector = CSSSelector('.score')
        match = tree.xpath(selector.path)
        rating = float(match[0].text)
        return rating
