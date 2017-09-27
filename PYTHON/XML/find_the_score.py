#!/usr/bin/env python3

import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    attr_cnt = 0
    for child in root.iter():
        attr_cnt += len(child.attrib)
    return attr_cnt


if __name__ == '__main__':
    # sys.stdin.readline()
    # xml = sys.stdin.read()
    N = int(input())
    xml = ""
    for _ in range(N):
        xml = '%s\n%s' % (xml, input())
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
