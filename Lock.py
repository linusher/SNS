import threading

class RWLock():
	def __init__(self):
		self.state='N'
		self.statelock=threading.Lock()
		self.rcount=0
		self.wcount=0
		self.rlock=threading.Lock()
		self.wlock=threading.Lock()
		self.wrlock=threading.Lock()
		self.selflock=threading.Lock()
	def acquireW(self):
		if self.state!='W':
			self.selflock.acquire()
			if self.state!='W':
				self.state='W'
			self.selflock.release()
		if self.wcount<=0:
			self.wrlock.acquire()
		self.selflock.acquire()
		self.wcount+=1
		self.selflock.release()
		self.wlock.acquire()
	def acquireR(self):
		self.rlock.acquire()
		if self.state!='R' or self.rcount<=0:
			self.wrlock.acquire()
		self.rlock.release()
		if self.state!='R':
			self.selflock.acquire()
			if self.state!='R':
				self.state='R'
			self.selflock.release()
		self.selflock.acquire()
		self.rcount+=1
		self.selflock.release()
	def releaseW(self):
		self.selflock.acquire()
		self.wcount-=1
		self.selflock.release()
		if self.wcount<0:
			self.wcount=0
		else:
			self.wlock.release()
		if self.wcount==0 and self.state=='W':
			self.selflock.acquire()
			if self.state=='W':
				self.state='N'
				self.wrlock.release()
			self.selflock.release()
	def releaseR(self):
		self.selflock.acquire()
		self.rcount-=1
		self.selflock.release()
		if self.rcount<=0:
			self.rcount=0
		if self.rcount==0:
			if self.state!='N':
				self.wrlock.release()
			if self.state=='R':
				self.selflock.acquire()
				if self.state=='R':
					self.state='N'
				self.selflock.release()

