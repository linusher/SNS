from Lock import RWLock
from threading import Thread
import threading
l=RWLock()

class A(Thread):
	def __init__(self,start,seconds,roll,text):
		Thread.__init__(self)
		self.s=seconds
		self.r=roll
		self.t=text
		self.st=start
	def run(self):
		threading._sleep(self.st)
		print self.t+" s"
		if self.r=='W':
			l.acquireW()
			print self.t+" start"
			threading._sleep(self.s)
			print self.t+" done"
			l.releaseW()
		elif self.r=='R':
			l.acquireR()
			print self.t+" start"
			threading._sleep(self.s)
			print self.t+" done"
			l.releaseR()
def printinfo(v):
	print "s:%s,rc:%d,wc:%d"%(v.state,v.rcount,v.wcount)
A(0,5,'R','R1').start()
A(1,5,'R','R2').start()
A(3,5,'W','W1').start()
A(5,5,'W','W2').start()
A(4,5,'R','R3').start()
A(9,10,'W','W3').start()
