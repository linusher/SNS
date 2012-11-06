import UI
import Client

from java.awt.event import ActionListener

class AcL(ActionListener):
	def actionPerformed(self,e):
		print e.getActionCommand()
		comm=e.getActionCommand()
		if comm=='Connect':
			rsp=Client.login(frame.getServerAddress(),frame.getUserName(),'9999')
			frame.addMsg(rsp)
			if rsp=='success':
				e.getSource().setEnabled(False)
				Client.requestUserList(frame.getServerAddress())
				for u in Client.userlist.keys():
					frame.addUser(u)
		elif comm=='Send':
			print frame.getSelectedUser()
			Client.sendmsg(frame.getMessage(),frame.getSelectedUser())
		elif comm=='Exit':
			frame.dispose()

frame=UI.MainFrameImp()
frame.setButtonListener(AcL())
frame.show()
