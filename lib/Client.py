import socket
import random
import UI
import threading
from java.awt.event import ActionListener
from java.lang import Thread

def getTCPSocket(target):
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(target)
	return s

def login(saddr,name,port):
	sock=getTCPSocket((saddr,8000))
	msg=[]
	msg.append('login\n')
	msg.append(name+'\n')
	msg.append(port+'\n')
	writer=sock.makefile('w')
	writer.writelines(msg)
	writer.flush()
	reader=sock.makefile('r')
	return reader.read().strip().lower()

def requestUserList(saddr):
	sock=getTCPSocket((saddr,8000))
	msg='requestuserlist\n'
	sock.send(msg)
	reader=sock.makefile('r')
	exec('ul='+reader.read())
	return ul

def getUDPSocket():
	return socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

def sendmsg(msg,user):
	global userlist
	getUDPSocket().sendto(msg,chg(userlist[user]))
def chg(hp):
	return (hp[0],int(hp[1]))
class AcL(ActionListener):
	def actionPerformed(self,e):
		global userlist
		print e.getActionCommand()
		comm=e.getActionCommand()
		if comm=='Connect':
			rsp=login(frame.getServerAddress(),frame.getUserName(),str(port))
			frame.addMsg(rsp)
			if rsp=='success':
				e.getSource().setEnabled(False)
				RULThread().start()
				SendHeartbeatThread().start()
		elif comm=='Send':
			#print frame.getSelectedUser()
			#print userlist
			fromUser=frame.getUserName()
			msg=frame.getMessage()
			toUser=frame.getSelectedUser()
			sendmsg(fromUser+":\n"+msg,toUser)
			frame.addMsg("you say:"+msg)
		elif comm=='Exit':
			frame.dispose()
			global runing
			runing=False
		elif comm=='Stop':
			pass
def refleshUserList():
	global userlist
	olduserlist=userlist.copy()
	userlist=requestUserList(frame.getServerAddress())
	print olduserlist
	print userlist
	for u in userlist.keys():
		if u!=frame.getUserName():
			if not olduserlist.has_key(u):
				frame.addUser(u)
	for u in olduserlist.keys():
		if not userlist.has_key(u):
			frame.removeUser(u)


class RULThread(Thread):
	def run(self):
		while runing:
			refleshUserList()
			Thread.sleep(5000)

class SendHeartbeatThread(Thread):
	def __init__(self):
		Thread.__init__(self)
	def run(self):
		while runing:
			host=frame.getServerAddress()
			user=frame.getUserName()
			getUDPSocket().sendto(user,(host,8001))	
			Thread.sleep(1000)

def acceptMsg():
	global sock
	while runing:
		try:
			data=sock.recv(4096)
			frame.addMsg(data)
		except:
			pass
runing=True
userlist={}
port=random.randrange(10000,65535)
while True:
	try:
		sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		sock.bind(('127.0.0.1',port))
		sock.settimeout(1)
		break
	except:
		pass
listenthread=threading.Thread(target=acceptMsg)
listenthread.daemon=True
listenthread.start()
frame=UI.MainFrameImp()
frame.setButtonListener(AcL())
frame.show()
