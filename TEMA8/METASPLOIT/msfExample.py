# -*- encoding: utf-8 -*-
import msfrpc
import time

client = msfrpc.Msfrpc({'uri':'/msfrpc', 'port':'8000', 'host':'0.0.0.0', 'ssl': True})
auth = client.login('usuario','password')
ip='0.0.0.0'

def processData(consoleId):
    while True:
        readedData = client.call('console.read',[consoleId])
        print readedData['data']
        if len(readedData['data']) > 1:
            print readedData['data']
        if readedData['busy'] == True:
            time.sleep(1)
            continue
        break
    
if auth:
    console = client.call('console.create')
    print console
    
    #SSH
    #auxiliary/scanner/ssh/cerberus_sftp_enumusers
    cmdSSHenumUsers = """auxiliary/scanner/ssh/cerberus_sftp_enumusers
    set RHOSTS """+ip
    
    cmdSSHenumUsers = cmdSSHenumUsers +"""\nrun 
    """
    print cmdSSHenumUsers
    
    print client.call('console.write',[console['id'],cmdSSHenumUsers])
    processData
    
    #auxiliary/scanner/ssh/detect_kippo
    cmdSSHkippo = """auxiliary/scanner/ssh/detect_kippo
    set RHOSTS """+ip
    
    cmdSSHkippo = cmdSSHkippo +"""\nrun 
    """
    print cmdSSHkippo
    
    print client.call('console.write',[console['id'],cmdSSHkippo])
    processData(console['id'])
    
    #auxiliary/scanner/ssh/ssh_enumusers
    cmdSSHenumUsers = """auxiliary/scanner/ssh/ssh_enumusers
    set RHOSTS """+ip
    
    cmdSSHenumUsers = cmdSSHenumUsers +"""\nrun 
    """
    print cmdSSHenumUsers
    
    print client.call('console.write',[console['id'],cmdSSHenumUsers])
    processData(console['id'])
    
    #auxiliary/scanner/ssh/ssh_identify_pubkeys
    cmdSShpubkeys = """auxiliary/scanner/ssh/ssh_identify_pubkeys
    set RHOSTS """+ip
    
    cmdSShpubkeys = cmdSShpubkeys +"""\nrun 
    """
    print cmdSShpubkeys
    
    print client.call('console.write',[console['id'],cmdSShpubkeys])
    processData(console['id'])
    
    #auxiliary/scanner/ssh/ssh_login
    cmdSShLogin = """auxiliary/scanner/ssh/ssh_login
    set RHOSTS """+ip
    
    cmdSShLogin = cmdSShLogin +"""\nrun 
    """
    print cmdSShLogin
    
    print client.call('console.write',[console['id'],cmdSShLogin])
    processData(console['id'])
    
    #auxiliary/scanner/ssh/ssh_login_pubkey
    cmdSShLoginPubKey = """auxiliary/scanner/ssh/ssh_login_pubkey
    set RHOSTS """+ip
    
    cmdSShLoginPubKey = cmdSShLoginPubKey +"""\nrun 
    """
    print cmdSShLoginPubKey
    
    print client.call('console.write',[console['id'],cmdSShLoginPubKey])
    processData(console['id'])
    
    #auxiliary/scanner/ssh/ssh_version
    cmdSShVersion = """auxiliary/scanner/ssh/ssh_version
    set RHOSTS """+ip
    
    cmdSShVersion = cmdSShVersion +"""\nrun 
    """
    print cmdSShVersion
    
    print client.call('console.write',[console['id'],cmdSShVersion])
    processData(console['id'])
    
    #auxiliary/scanner/ssh/ssh_version
    cmdSShVersion = """auxiliary/scanner/ssh/ssh_version
    set RHOSTS """+ip
    
    cmdSShVersion = cmdSShVersion +"""\nrun 
    """
    print cmdSShVersion
    
    print client.call('console.write',[console['id'],cmdSShVersion])
    processData(console['id'])
    
    #SSL
    #auxiliary/gather/impersonate_ssl
    cmdSSLimpersonate = """auxiliary/gather/impersonate_ssl
    set RHOSTS """+ip
    
    cmdSSLimpersonate = cmdSSLimpersonate +"""\nrun 
    """
    print cmdSSLimpersonate
    
    print client.call('console.write',[console['id'],cmdSSLimpersonate])
    processData(console['id'])
    
    #auxiliary/scanner/http/ssl
    cmdSSLhttp = """auxiliary/scanner/http/ssl
    set RHOSTS """+ip
    
    cmdSSLhttp = cmdSSLhttp +"""\nrun 
    """
    print cmdSSLhttp
    
    print client.call('console.write',[console['id'],cmdSSLhttp])
    processData(console['id'])
    
    #auxiliary/scanner/http/ssl_version
    cmdSSLversion = """auxiliary/scanner/http/ssl_version
    set RHOSTS """+ip
    
    cmdSSLversion = cmdSSLversion +"""\nrun 
    """
    print cmdSSLversion
    
    print client.call('console.write',[console['id'],cmdSSLversion])
    processData(console['id'])