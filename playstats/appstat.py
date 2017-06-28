from urllib.request import urlopen
from lxml import html
from lxml.cssselect import CSSSelector


class AppStat:
    def __init__(self, package_name):
        self.app_url = "https://play.google.com/store/apps/details?id=%s" % package_name
        self.content = urlopen(self.app_url).read()
        self.tree = html.fromstring(self.content)

    def get_rating(self):
        selector = CSSSelector('.score')
        match = self.tree.xpath(selector.path)
        rating = float(match[0].text)
        return rating

    def get_all_ratings(self):
        # Returns number of ratings corresponding to different stars
        # in the form of dictionary.
        selector = CSSSelector('.bar-number')
        matches = self.tree.xpath(selector.path)
        ratings = [int(x.text.replace(',', '')) for x in matches]
        ratings_dict = {star: no_of_ratings for (star, no_of_ratings) in zip(range(5, 0, -1), ratings)}
        return ratings_dict
