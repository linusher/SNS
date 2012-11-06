import socket
import threading

class ListenThread(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.sock.bind(('127.0.0.1',8888))
		self.sock.listen(65535)
	def run(self):
		while True:
			(s,a)=self.sock.accept()
			print a
			c=ClientHandleThread(s)
			c.daemon=True
			c.start()

class ClientHandleThread(threading.Thread):
	def __init__(self,s):
		threading.Thread.__init__(self)
		self.sock=s
	def run(self):
		while True:
			print self.sock.recv(1024)

class SocketReader():
	def __init__(self,s):
		self.sock=s;
	def readline(self):
		result=''
		recvData=self.sock.recv(1)
		while recvData!='' && recvData!='\n':
			result+=recvData
			recvData=self.sock.recv(1)
		if recvData=='':
			print self.sock.getsockname()+" has been offline!"
			self.sock.shutdown(socket.SHUT_RDWR)
			self.sock.close
		return result
			


ListenThread().start()
