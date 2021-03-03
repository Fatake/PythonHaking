import urllib2
proxies = {'http': 'http://10.129.8.100:8080'}
print "Using HTTP proxy %s" % proxies['http']
response = urllib2.urlopen("http://www.google.com")
response.geturl()
response.getcode()
response.headers.keys()
response.headers.values()
for header,value in response.headers.items():
	print header + ":" + value


import urllib3
pool = urllib3.PoolManager(10)
connection = urllib3.connection_from_url('http://www.google.com')
response = connection.request('GET','http://www.google.com')
print response.status
response.headers.keys()
response.headers.values()
for header,value in response.headers.items():
	print header + ":" + value
