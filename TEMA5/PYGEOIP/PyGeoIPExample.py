# -*- encoding: utf-8 -*-

import pygeoip
import pprint

gi = pygeoip.GeoIP('GeoLiteCity.dat')
gi2 = pygeoip.GeoIP('GeoIPASNum.dat')
giIPv6 = pygeoip.GeoIP('GeoIPv6.dat')

pprint.pprint("Country code by addr: %s " %(str(gi.country_code_by_addr('173.194.34.192'))))
pprint.pprint("Country code by name: %s " %(str(gi.country_code_by_name('google.com'))))
pprint.pprint("Country name by addr: %s " %(str(gi.country_name_by_addr('173.194.34.192'))))
pprint.pprint("Country name by name: %s " %(str(gi.country_name_by_name('google.com'))))

pprint.pprint("Organization by addr: %s " %(str(gi2.org_by_addr('173.194.34.192'))))
pprint.pprint("Organization by name: %s " %(str(gi2.org_by_name('google.com'))))

pprint.pprint("Full record: %s " %(str(gi.record_by_addr('173.194.34.192'))) )

for record,value in gi.record_by_addr('173.194.34.192').items():
	print record + "-->" + str(value)
	
pprint.pprint("Timezone: %s" %(str(gi.time_zone_by_addr('173.194.34.192'))) )
