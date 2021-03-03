#!/usr/bin/python

import httplib

host = "192.168.56.101"

req = httplib.HTTP(host)
req.putrequest("HEAD", "/")
req.putheader("Host", host)
req.endheaders()
req.send("")

statusCode, statusMsg, headers = req.getreply()
print("Status code: ", statusCode)
print("Status msg: ", statusMsg)
print("headers: ", headers)