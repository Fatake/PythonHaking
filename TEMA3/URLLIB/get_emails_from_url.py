import urllib2
import re

web =  raw_input("Url: ")

respuesta = urllib2.Request('http://'+web)

pagina = urllib2.urlopen(respuesta).read()
#esto complia la exprsion siguiente
patron = re.compile("[-a-zA-Z0-9._]+@[-a-zA-Z0-9_]+.[a-zA-Z0-9_.]+")
#se explica por si mismo 
smails = re.findall(patron,pagina)
listaemails = open ('emails.txt', 'a+')
d2 = str(smails)
listaemails.write(d2)
listaemails.close()
print "e-mails guadados en el fichero emails.txt"
