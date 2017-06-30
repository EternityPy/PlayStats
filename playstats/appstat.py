from urllib.request import urlopen
from lxml import html
from lxml.cssselect import CSSSelector


class AppStat:
    def __init__(self, package_name):
        self.app_url = "https://play.google.com/store/apps/details?id=%s" % package_name
        self.content = urlopen(self.app_url).read()
        self.tree = html.fromstring(self.content)

    def rating(self):
        # Returns rating out of 5
        selector = CSSSelector('.score')
        match = self.tree.xpath(selector.path)
        rating = float(match[0].text)
        return rating

    def all_ratings(self):
        # Returns number of ratings corresponding to different stars
        # in the form of dictionary.
        selector = CSSSelector('.bar-number')
        matches = self.tree.xpath(selector.path)
        ratings = [int(x.text.replace(',', '')) for x in matches]
        ratings_dict = {star: no_of_ratings for (star, no_of_ratings) in
                        zip(range(5, 0, -1), ratings)}
        return ratings_dict

    def total_reviews(self):
        # Returns total number of reviews for an app.
        selector = CSSSelector('.reviews-num')
        match = self.tree.xpath(selector.path)
        total_reviews = int(match[0].text.replace(',', ''))
        return total_reviews

    def vendor(self):
        # Returns the vendor of the app.
        selector = CSSSelector('span[itemprop="name"]')
        match = self.tree.xpath(selector.path)
        vendor = match[0].text
        return vendor

    def last_updated(self):
        # Returns the last updated date for the app.
        selector = CSSSelector('div.content[itemprop="datePublished"]')
        match = self.tree.xpath(selector.path)
        last_updated = match[0].text
        return last_updated

    def genre(self):
        # Returns the genre that the app belongs to.
        selector = CSSSelector('[itemprop="genre"]')
        match = self.tree.xpath(selector.path)
        genre = match[0].text
        return genre

    def version(self):
        # Returns the genre that the app belongs to.
        selector = CSSSelector('div.content[itemprop="softwareVersion"]')
        match = self.tree.xpath(selector.path)
        if len(match) == 1:
            return match[0].text.strip()
        return 'Unavailable'

    def android_version(self):
        # Returns the minimum android version the app requires to run.
        selector = CSSSelector('div.content[itemprop="operatingSystems"]')
        match = self.tree.xpath(selector.path)
        if len(match) == 1:
            return match[0].text.strip()
        return 'Unavailable'

    def size(self):
        # Returns the size of the app.
        selector = CSSSelector('div.content[itemprop="fileSize"]')
        match = self.tree.xpath(selector.path)
        if len(match) == 1:
            return match[0].text.strip()
        return 'Unavailable'
