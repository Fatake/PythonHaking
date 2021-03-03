#!/usr/bin/python

import urllib2
from HTMLParser import HTMLParser

class myParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if (tag == "a"):
            for a in attrs:
                if (a[0] == 'href'):
                    link = a[1]	
                    if (link.find('http') >= 0):
                        print(link)
                        newParse = myParser()
                        newParse.feed(link)
						

web =  raw_input("Url: ")
url = "http://"+web

#without proxy
request = urllib2.Request(url)
handle = urllib2.urlopen(request)

#with proxy
proxy =  raw_input("Proxy[IP:PORT]: ")

proxy = urllib2.ProxyHandler({'http': proxy})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)
handle = urllib2.urlopen(url)

parser = myParser()
parser.feed(handle.read().decode('utf-8'))




