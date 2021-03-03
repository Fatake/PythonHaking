from scapy.all import sr1, IP, TCP


def analyze_port(host, port):
'''
Funcion que determina el estado de un puerto: Abierto/cerrado
:param host: target
:param port: puerto a comprobar
:type port: int
'''
    OPEN_PORTS = []
    print "[ii] Analizando el puerto %s" % port
    res = sr1(IP(dst=host)/TCP(dport=port), verbose=False, timeout=0.2)
        if res is not None and TCP in res:
            if res[TCP].flags == 18:
                OPEN_PORTS.append(port)
                print "Puerto %s abierto " % port


def main():
    for x in xrange(0, 80):
        analyze_port("domain", x)
            print "[*] Puertos abiertos:"
    for x in OPEN_PORTS:
        print " - %s/TCP" % x
        
