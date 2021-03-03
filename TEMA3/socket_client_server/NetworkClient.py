#!/usr/bin/python3

import socket

host='localhost'
port = 5000

mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr=(host,port)
mysock.connect(addr)


try:
	print 'Conntencted to host '+str(host)+' in port: '+str(port)
	msg=b"hi, this is a test\n"
	mysock.sendall(msg)
except socket.errno as e:
    print("Socket error ", e)
finally:
    mysock.close()

