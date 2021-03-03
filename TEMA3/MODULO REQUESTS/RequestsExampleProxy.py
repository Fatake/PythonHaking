# -*- encoding: utf-8 -*-

import requests, json

print "Requests Library tests."

http_proxy  = ""
https_proxy = ""

proxyDict = { "http"  : http_proxy, "https" : https_proxy}
			
responseGet = requests.get("http://www.google.es",proxies=proxyDict)

print responseGet.text.encode('utf-8')

print responseGet.json

print responseGet.encoding

print responseGet.content

print "Status code: "+str(responseGet.status_code)

print "Headers response: "
for header, value in responseGet.headers.items():
  print(header, '-->', value)
  
print "Headers request : "
for header, value in responseGet.request.headers.items():
  print(header, '-->', value)