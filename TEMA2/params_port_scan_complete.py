import argparse


if __name__ == "__main__":

    description = """ Ejemplos de uso:
        + Escaneo basico:
             -target 127.0.0.1
        + Indica un puerto especifico:
             -target 127.0.0.1 -port 21
        + Indica una lista de puertos:
             -target 127.0.0.1 -port 21,22
        + Solo mostrar puertos abiertos
             -target 127.0.0.1 --open True """

    parser = argparse.ArgumentParser(description='Port scanning', epilog=description,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-target", metavar='TARGET', dest="target", help="target to scan",required=True)
    parser.add_argument("-ports", dest="ports", 
                        help="Please, specify the target port(s) separated by comma[80,8080 by default]",
                        default = "80,8080")    
    parser.add_argument('-v', dest='verbosity', default=0, action="count",
                        help="verbosity level: -v, -vv, -vvv.")
    parser.add_argument("--open", dest="only_open", action="store_true",
                        help="only display open ports", default=False)
   

    params = parser.parse_args()
    
    portlist = params.ports.split(',')
    print params.ports
    print portlist
    for port in portlist:
        print "Puerto:" + port
