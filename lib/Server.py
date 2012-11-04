import SocketServer
import threading
import time

userlistlock=threading.Lock()
userheartbeatlock=threading.Lock()
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
			print sock.getsockname()+" request to login in"
			username=reader.readline().strip().lower()
			addr=reader.readline().strip.lower()
			port=reader.readline().strip.lower()

			userlistlock.acquire()
			userlist[username]=(addr,port)
			userlistlock.release()

			userheartbeatlock.acquire()
			userheartbeat[username]=time.time()
			userheartbeatlock.release()
			print sock.getsockname()+" have login in username is:"+username
		elif command=='request online user list':
			pass		
		
		elif command=='':
			pass
		while True:
			pass

class HeartbeatHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		sock=self.request	


requestThread=threading.Thread(target=SocketServer.ThreadingTCPServer(('127.0.0.1',8000),RequestHandler).serve_forever)
requestThread.daemon=True
requestThread.start()

#heartbeatThread=threading.Thread(target=SocketServer.ThreadingUDPServer(('127.0.0.1',8001),HeartbeatHandler).serve_forever)
#heartbeatThread.daemon=True;
#heartbeatThread.start()
SocketServer.ThreadingUDPServer(('127.0.0.1',8001),HeartbeatHandler).serve_forever();


