import argparse

parser = argparse.ArgumentParser(description='params port scan')
parser.add_argument("-t", dest="target", help="target", required=True)
parser.add_argument("-p", "--port", dest="port", type=int, default=80,
    help="port to scan. Default: 80.")
parser.add_argument('-v', dest='verbosity', help='verbosity level', type=int, default=0)
parser.add_argument("--open", dest="only_open", action="store_true",
    help="only display open ports", default=False)


params = parser.parse_args()

print "Target :",params.target
print "Port %:",params.port
print "Verbosity :",params.verbosity
print "Only open :",params.only_open
