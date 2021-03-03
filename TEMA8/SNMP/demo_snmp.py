from snmp_helper import snmp_get_oid,snmp_extract
COMMUNITY_STRING = 'public'
SNMP_HOST = '71.180.188.152'
SNMP_PORT = 161
a_device = (SNMP_HOST, COMMUNITY_STRING, SNMP_PORT)
snmp_data = snmp_get_oid(a_device, oid='.1.3.6.1.2.1.1.1.0', display_errors=True)
print snmp_data
if snmp_data is not None:
	output = snmp_extract(snmp_data)
	print output