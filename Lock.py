import threading

#read and write lock writing first
#state N=>NO writer or reader; W=>writing; R=>reading
#rcount:numbers of read require
#wcount:numbers of write require
class RWLock():
	def __init__(self):
		self.state='N'
		self.rcount=0
		self.wcount=0
		self.rlock=threading.Lock()
		self.wlock=threading.Lock()
		self.wrlock=threading.Lock()
		self.selflock=threading.Lock()
		self.wwlock=threading.Lock()
	def acquireW(self):
		#change state to W to tell want to W and the reader come after will be blocked
		if self.state!='W':
			self.selflock.acquire()
			if self.state!='W':
				self.state='W'
			self.selflock.release()
		self.wwlock.acquire()
		#try to get the wrlock if have got, skip this step
		if self.wcount<=0:
			self.wrlock.acquire()
		self.selflock.acquire()
		self.wcount+=1
		self.selflock.release()
		self.wwlock.release()
		self.wlock.acquire()
	def acquireR(self):
		self.rlock.acquire()
		#try to get the wrlock if have got, skip this step
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
		#while no writer release wrlock and change state to N
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
		#while no reader release wrlock and change state to N
		if self.rcount==0:
			if self.state!='N':
				self.wrlock.release()
			if self.state=='R':
				self.selflock.acquire()
				if self.state=='R':
					self.state='N'
				self.selflock.release()

