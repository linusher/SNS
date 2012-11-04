import socket
import SocketServer
import random
import Singleton
import threading

userList={}
serverSocket=None

def getTCPSocket(target):
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(target)
	return s

class MessageHandler(SocketServer.BaseRequestHandler):
	pass


@singleton
class SendHeartbeatThread(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)

