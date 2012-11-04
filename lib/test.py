from javax.swing import AbstractAction
from UI import MainFrameImp

class ButtonAction(AbstractAction):
	def __init__(self,mfi):
		self.mfi=mfi
	def actionPerformed(self,e):
		print e.getID()
		self.mfi.addUser("Fuck you")

m=MainFrameImp()
m.getB_connect().addActionListener(ButtonAction(m))
m.show()
