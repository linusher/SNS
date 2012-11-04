package UI;

public interface IMainFrame {
	public void addUser(String name);
	public void addMsg(String msg);
	public void removeUser(String name);
	public String getServerAddress();
	public String getUserName();
	public String getMessage();
	public String getSelectedUser();
}
