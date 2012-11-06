import SocketServer
import threading
import time
import Lock

userlistlock=Lock.RWLock()
userheartbeatlock=Lock.RWLock()
userlist={}
userheartbeat={}

#handle the requests from client
class RequestHandler(SocketServer.StreamRequestHandler):
	def handle(self):
		reader=self.rfile;#get the file like input
		writer=self.wfile;#get the file like output
		sock=self.request#get the request socket
		command=reader.readline().strip().lower()
		if command=='login':
			print str(sock.getsockname())+" request to login in"
			username=reader.readline().strip().lower()
			addr=sock.getsockname()[0]
			port=reader.readline().strip().lower()
			userlistlock.acquireR()
			if userlist.has_key(username):
				print username+" has been exist"
				writer.write(username+" has been used!\n")
				userlistlock.releaseR()
				return
			userlistlock.releaseR()
			
			userlistlock.acquireW()
			userlist[username]=(addr,port)
			userlistlock.releaseW()

			userheartbeatlock.acquireW()
			userheartbeat[username]=time.time()
			userheartbeatlock.releaseW()
			print userlist
			print userheartbeat
			print str(sock.getsockname())+" have login in username is:"+username
			writer.write('success')
			writer.flush()
		elif command=='requestuserlist':
			print str(sock.getsockname())+" request to get user list"
			userlistlock.acquireR()
			writer.write(str(userlist))
			userlistlock.releaseR()
			writer.flush()
		elif command=='connect':
			pass

class HeartbeatHandler(SocketServer.BaseRequestHandler):
	def handle(self):	
		username=self.request[0].strip().lower()
		print username+" send heart beat"
		userheartbeatlock.acquireW()
		userheartbeat[username]=time.time()
		userheartbeatlock.releaseW()


def checkOnline():
	while True:
		currtime=time.time()
		userheartbeatlock.acquireR()
		hbs=userheartbeat.copy()
		userheartbeatlock.releaseR()
		print hbs
		for u in hbs.items():
			if currtime-u[1]>5:
				userheartbeatlock.acquireW()
				userheartbeat.pop(u[0])
				userheartbeatlock.releaseW()
				userlistlock.acquireW()
				userlist.pop(u[0])
				userlistlock.releaseW()
				print u[0]+" is offline"
		threading._sleep(5)
		
requestThread=threading.Thread(target=SocketServer.ThreadingTCPServer(('127.0.0.1',8000),RequestHandler).serve_forever)
requestThread.daemon=True
requestThread.start()

checkthread=threading.Thread(target=checkOnline)
checkthread.daemon=True
checkthread.start()

#heartbeatThread=threading.Thread(target=SocketServer.ThreadingUDPServer(('127.0.0.1',8001),HeartbeatHandler).serve_forever)
#heartbeatThread.daemon=True;
#heartbeatThread.start()
SocketServer.ThreadingUDPServer(('127.0.0.1',8001),HeartbeatHandler).serve_forever();

