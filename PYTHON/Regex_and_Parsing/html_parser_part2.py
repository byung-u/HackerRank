#!/usr/bin/env python3
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_data(self, tag):
        if tag == '\n':
            return
        print('>>> Data\n{:s}'.format(tag))

    def handle_comment(self, tag):
        t = tag.split('\n')
        if len(t) == 1:
            print('>>> Single-line Comment\n{:s}'.format(tag))
        else:
            print('>>> Multi-line Comment')
            for s in t:
                print(s)


MyParser = MyHTMLParser()
MyParser.feed('\n'.join([input().strip() for _ in range(int(input()))]))
