#!/usr/bin/python
# tcpclient.py
 
import socket
import httplib

host="127.0.0.1"
port = 1337

try:
	mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	mysocket.connect((host, port))
	print 'Conectado al host '+str(host)+' en el puerto: '+str(port)
	mysocket.send("Hello\n")
	message = mysocket.recv(1024)
	print "Received", message
	msg="Message from the Client\n"
	mysocket.sendall(msg)
except socket.errno as e:
	print("Socket error ", e)
finally:
	mysocket.close()