#!/usr/bin/env python3

import sys
import xml.etree.ElementTree as etree

    
#from xml.etree.ElementTree import XMLParser
#class MaxDepth:                     # The target object of the parser
#    maxDepth = 0
#    depth = 0
#    def start(self, tag, attrib):   # Called for each opening tag.
#        self.depth += 1
#        if self.depth > self.maxDepth:
#            self.maxDepth = self.depth
#    def end(self, tag):             # Called for each closing tag.
#        self.depth -= 1
#    def data(self, data):
#        pass            # We do not need to do anything with data.
#    def close(self):    # Called when all data has been parsed.
#        return self.maxDepth

maxdepth = -1
def depth(elem, level):
    global maxdepth
    if level == maxdepth:
        maxdepth += 1

    for child in elem:
        depth(child, level+1)

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"

    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
    ################
    # 1st solution
    ################
    # target = MaxDepth()
    # parser = XMLParser(target=target)
    # parser.feed(xml)
    # print(parser.close())
