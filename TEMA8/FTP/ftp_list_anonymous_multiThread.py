#!/usr/bin/env python

import threading
import Queue
import time
import ftplib
import shodan
import socket

#lock = threading.Lock()

class WorkerThread(threading.Thread) :


	def __init__(self, queue, tid) :
		threading.Thread.__init__(self)
		self.queue = queue
		self.tid = tid
		print "Worker %d Reporting "%self.tid



	def run(self) :
		lock = threading.Lock()

		while True :
			lock.acquire()
			host = None

			try:
				site = self.queue.get(timeout=1)
				server_name = socket.gethostbyaddr(str(site))

			except Queue.Empty :
				print "Worker %d exiting... "%self.tid

			try:
				print "Connecting to ip: " +site+ " / Server name:" + server_name[0]
				ftp = ftplib.FTP(site)
				ftp.login()
				print "Connection to server_name %s" %server_name[0]
				print ftp.retrlines('LIST')
				ftp.quit()
				print "Existing to server_name %s" %server_name[0]
			except Exception,e:
				print str(e)
				print "Error in listing %s" %server_name[0]

			finally:
				lock.release() 


			#print "Finished logging into ftp site %s"%site
			self.queue.task_done()



queue = Queue.Queue()

sites =[]

shodanKeyString = 'v4YpsPUJ3wjDxEqywwu6aF5OZKWj8kik'
shodanApi = shodan.Shodan(shodanKeyString)
results = shodanApi.search("port: 21 Anonymous user logged in")

for match in results['matches']:
	if match['ip_str'] is not None:
		sites.append(match['ip_str'])
    

threads = []			
for i in range(4) :
	print "Creating WorkerThread : %d"%i
	worker = WorkerThread(queue, i)
	worker.setDaemon(True)
	worker.start()
	threads.append(worker)
	print "WorkerThread %d Created!"%i 	

for site in sites :
	queue.put(site)	

queue.join()

print "All Tasks over!"	
