#!/usr/bin/python

import urllib
import re

class hnx:
    def __init__(self):
        self.url = 'https://news.ycombinator.com/rss'
        self.color = Colors()
    def main(self):
        src = urllib.urlopen(self.url).read()
        items = re.findall(r"<item>(.*?)</item>", src)
        for x in items:
            title = ' '.join(re.findall(r"<title>(.*?)</title>", x))
            url = ' '.join(re.findall(r"<link>(.*?)</link>", x))
            print self.color.color(text=title, color='red', other='bold'), self.color.color(text='-', other='bold'), self.color.color(text=url, color='blue', other='bold')


class Colors():
    def __init__(self):
        self.colors = {"grey":'30',"red":'31', "green":'32',"yellow":'33',"blue":'34', 'magenta':'35','cyan':'36', 'white':'37'}
        self.other = {"bold":'1', 'dark':'2','underline':'4', 'highlight':'7', 'hide':'8'}
        self.highlights = {"grey":'40','red':41,'green':'42','yellow':'43','blue':'44','magenta':'45','cyan':'46', 'white':'47'}
    def color(self, color=None, highlight=None, text=None, other=None):
        if color:
            text = "\033[{0}m{1}".format(self.colors[color], text)
        if highlight:
            text = "\033[{0}m{1}".format(self.highlights[highlight], text)
        if other:
            text = "\033[{0}m{1}".format(self.other[other], text)
        return text + "\033[0m"

if __name__ == "__main__":
    hnx().main()
