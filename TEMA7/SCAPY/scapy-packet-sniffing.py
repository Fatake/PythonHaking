import scapy, GeoIP
from scapy import *
gi = GeoIP.new(GeoIP.GEOIP_MEMORY_CACHE)

def prnPkt(pkt):
    src=pkt.getlayer(IP).src
    dst=pkt.getlayer(IP).dst
    srcCo = gi.country_code_by_addr(src)
    dstCo = gi.country_code_by_addr(dst)
    print srcCo+">>"+dstCo
    try:
        while True:
            sniff(filter="ip",prn=prnPkt,store=0)
    except KeyboardInterrupt:
        print "\nExiting.\n"