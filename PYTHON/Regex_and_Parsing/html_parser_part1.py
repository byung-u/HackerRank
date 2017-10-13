#!/usr/bin/env python3
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('Start :', tag)
        for ele in attrs:
            print('->', ele[0], '>', ele[1])

    def handle_endtag(self, tag):
        print('End   :', tag)

    def handle_startendtag(self, tag, attrs):
        print('Empty :', tag)
        for ele in attrs:
            print('->', ele[0], '>', ele[1])


MyParser = MyHTMLParser()
MyParser.feed(''.join([input().strip() for _ in range(int(input()))]))

# It was failed
'''
html_parse = re.compile("""
                       # beginning of string
    (?<=\<)   #
    (\!\-\-\ |\ \-\-|[\w]+|\/[\w]+|[\w\ \/]+|[\w\s\d\'\=\-\"\#\&\%\$\+\,\;]+)   #
    (?=\>)    #
                       # end of string
    """ ,re.VERBOSE|re.MULTILINE)

temp = []
for _ in range(int(input())):
    temp.append(input())
s = '\n'.join(temp)
for f in html_parse.finditer(s):
    r = f.group()
    if re.match(r'^\/\w', r) is not None:
        # print('End\t:', r[1:])
        print('{:6s}: {:s}'.format('End', r[1:]))
    elif re.match(r'^[\w\W]+\ \/$', r) is not None:
        print('{:6s}: {:s}'.format('Empty', r[:-1].strip()))
    else:
        rs = r.split()
        if len(rs) == 1:
            # print('Start\t:', r)
            print('{:6s}: {:s}'.format('Start', r))
        else:
            for idx, check in enumerate(rs):
                if idx == 0:
                    print('{:6s}: {:s}'.format('Start', check))
                    continue
                rs2 = check.split('=')
                if len(rs2) == 1:
                    print('->', rs2[0], '> None')
                else:
                    result = '-> %s' % (' > '.join(rs2))
                    print(result.replace("'", ''))
'''
