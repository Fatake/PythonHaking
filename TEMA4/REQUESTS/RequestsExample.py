# -*- encoding: utf-8 -*-

import requests, json

print "Requests probando API REST"
#response = requests.get("http://api.openweathermap.org/data/2.5/weather?&q=&appid=0888d6d73eeb6588a5b5da08f4d32bb9",timeout=5)
#response = requests.get("http://httpbin.org/get?id=0123456789",timeout=5)

headers = {'user-agent': 'my-user-agent-header/v1.0'}

proxy = {
  "http": "10.129.8.100:8080",
}


datos = {
   'id': '0123456789',
}

files = {'file': ('agile.xlsx', open('agile.xlsx', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}

#response = requests.post("http://httpbin.org/post",timeout=5,data=datos)
response = requests.post("http://httpbin.org/post",data=datos,headers=headers)

print "Status code: "+str(response.status_code)

if response.status_code == 200:
   results = response.json()

   for result in results.items():
      print result
      
   print "Headers response: "
   for header, value in response.headers.items():
      print(header, '-->', value)
        
   print "Headers request : "
   for header, value in response.request.headers.items():
      print(header, '-->', value)
      
   print "Server:" + response.headers['server']
else:
   print "Error code %s" % response.status_code
   
