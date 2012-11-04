package UI;

public class MainFrameImp extends MainFrame implements IMainFrame {

	@Override
	public void addUser(String name) {
		// TODO Auto-generated method stub
		this.userList.addElement(name);
	}

	@Override
	public void addMsg(String msg) {
		// TODO Auto-generated method stub
		this.msglist.addElement(msg);
	}

	@Override
	public void removeUser(String name) {
		// TODO Auto-generated method stub
		this.userList.addElement(name);
	}

	@Override
	public String getServerAddress() {
		// TODO Auto-generated method stub
		return tx_svraddr.getText();
	}

	@Override
	public String getUserName() {
		// TODO Auto-generated method stub
		return tx_username.getText();
	}

	@Override
	public String getMessage() {
		// TODO Auto-generated method stub
		return tx_msg.getText();
	}

	@Override
	public String getSelectedUser() {
		// TODO Auto-generated method stub
		return (String)l_userlist.getSelectedValue();
	}
	
	
}
