# -*- encoding: utf-8 -*-

import sys
import socket
import dns

from ipwhois import IPWhois


if len(sys.argv) != 2:
    print "[-] usage python IPWHOISExample.py <domain_name>"
    sys.exit()

domain = sys.argv[1]
host = socket.gethostbyname(domain)
print host

#whois = IPWhois(host).lookup()
#print whois

addr = dns.reversename.from_address(host)
print addr