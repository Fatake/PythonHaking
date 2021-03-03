#!/usr/bin/python
# tcpserver.py
 
import socket

host = 'localhost'
port = 1337

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(10)

print 'Servidor escuchando peticiones en el puerto '+str(port)

while 1:
        cli,addr = sock.accept()
        print "Se ha producido una conexion desde", addr
        buf = cli.recv(1024)
        print "Received", buf
        if buf == "Hello\n":
                cli.send("Message from the server\n")
        cli.close()