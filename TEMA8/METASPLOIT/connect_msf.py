# -*- encoding: utf-8 -*-
import msfrpc
client = msfrpc.Msfrpc({'uri':'/msfrpc', 'port':'3790', 'host':'127.0.0.1', 'ssl': True})
auth = client.login('msfadmin','msfadmin')
if auth:
    print str(client.call('core.version'))+'\n'
    print str(client.call('core.thread_list', []))+'\n'
    print str(client.call('core.setg', ["RHOST", "192.168.1.244"]))+'\n'
    print str(client.call('job.list', []))+'\n'
    print str(client.call('module.exploits', []))+'\n'
    print str(client.call('module.auxiliary', []))+'\n'
    print str(client.call('module.post', []))+'\n'
    print str(client.call('module.payloads', []))+'\n'
    print str(client.call('module.encoders', []))+'\n'
    print str(client.call('module.nops', []))+'\n'
    print str(client.call('module.info', ["exploit", "multi/browser/java_jre17_jmxbean_2"]))+'\n'