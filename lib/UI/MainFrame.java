package UI;

import java.awt.BorderLayout;

import javax.swing.Box;
import javax.swing.DefaultListModel;
import javax.swing.JPanel;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.BoxLayout;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.Dimension;
import javax.swing.JList;
import java.awt.ComponentOrientation;
import java.awt.FlowLayout;
import java.awt.Rectangle;
import java.awt.GridLayout;
import javax.swing.BorderFactory;
import javax.swing.border.EtchedBorder;
import java.awt.event.KeyEvent;
import javax.swing.JScrollPane;
import java.awt.GridBagLayout;
import javax.swing.JSplitPane;
import java.awt.GridBagConstraints;

public class MainFrame extends JFrame {

	private static final long serialVersionUID = 1L;
	private JPanel jContentPane = null;
	private JPanel jPanel = null;
	protected JTextField tx_svraddr = null;
	private JLabel jLabel = null;
	private JLabel jLabel1 = null;
	protected JTextField tx_username = null;
	protected JButton b_connect = null;
	protected JButton b_stop = null;
	private JPanel jPanel1 = null;
	protected JList l_userlist = null;
	private JList l_msglist = null;
	protected DefaultListModel userList;  //  @jve:decl-index=0:visual-constraint="590,16"
	private JScrollPane jScrollPane = null;
	private JPanel jPanel4 = null;
	private JLabel jLabel2 = null;
	protected JButton jSend = null;
	protected JButton jExit = null;
	private JPanel jPanel5 = null;
	protected DefaultListModel msglist = null;  //  @jve:decl-index=0:visual-constraint="588,68"
	private JScrollPane jScrollPane1 = null;
	private JPanel jPanel2 = null;
	protected JTextField tx_msg = null;
	/**
	 * This is the default constructor
	 */
	public MainFrame() {
		super();
		initialize();
	}

	/**
	 * This method initializes this
	 * 
	 * @return void
	 */
	private void initialize() {
		this.setMinimumSize(new Dimension(550, 300));
		this.setBounds(new Rectangle(100, 100, 550, 300));
		this.setContentPane(getJContentPane());
		this.setTitle("JFrame");
	}

	/**
	 * This method initializes jContentPane
	 * 
	 * @return javax.swing.JPanel
	 */
	private JPanel getJContentPane() {
		if (jContentPane == null) {
			BorderLayout borderLayout = new BorderLayout();
			borderLayout.setHgap(10);
			borderLayout.setVgap(5);
			jContentPane = new JPanel();
			jContentPane.setLayout(borderLayout);
			jContentPane.add(getJPanel(), BorderLayout.NORTH);
			jContentPane.add(getJPanel1(), BorderLayout.WEST);
			jContentPane.add(getJScrollPane1(), BorderLayout.CENTER);
			jContentPane.add(getJPanel2(), BorderLayout.SOUTH);
		}
		return jContentPane;
	}

	/**
	 * This method initializes jPanel	
	 * 	
	 * @return javax.swing.JPanel	
	 */
	private JPanel getJPanel() {
		if (jPanel == null) {
			FlowLayout flowLayout = new FlowLayout();
			flowLayout.setAlignment(FlowLayout.RIGHT);
			flowLayout.setHgap(5);
			jLabel1 = new JLabel();
			jLabel1.setText("Name:");
			jLabel1.setDisplayedMnemonic(KeyEvent.VK_UNDEFINED);
			jLabel = new JLabel();
			jLabel.setText("ServerAddress:");
			jLabel.setPreferredSize(new Dimension(110, 15));
			jPanel = new JPanel();
			jPanel.setLayout(flowLayout);
			jPanel.setComponentOrientation(ComponentOrientation.LEFT_TO_RIGHT);
			jPanel.add(jLabel, null);
			jPanel.add(getTx_svraddr(), null);
			jPanel.add(jLabel1, null);
			jPanel.add(getTx_username(), null);
			jPanel.add(getB_connect(), null);
			jPanel.add(getB_stop(), null);
		}
		return jPanel;
	}

	/**
	 * This method initializes tx_svraddr	
	 * 	
	 * @return javax.swing.JTextField	
	 */
	private JTextField getTx_svraddr() {
		if (tx_svraddr == null) {
			tx_svraddr = new JTextField();
			tx_svraddr.setPreferredSize(new Dimension(80, 19));
		}
		return tx_svraddr;
	}

	/**
	 * This method initializes tx_username	
	 * 	
	 * @return javax.swing.JTextField	
	 */
	private JTextField getTx_username() {
		if (tx_username == null) {
			tx_username = new JTextField();
			tx_username.setPreferredSize(new Dimension(50, 19));
		}
		return tx_username;
	}

	/**
	 * This method initializes b_connect	
	 * 	
	 * @return javax.swing.JButton	
	 */
	public JButton getB_connect() {
		if (b_connect == null) {
			b_connect = new JButton();
			b_connect.setText("Connect");
			b_connect.setPreferredSize(new Dimension(100, 25));
		}
		return b_connect;
	}

	/**
	 * This method initializes b_stop	
	 * 	
	 * @return javax.swing.JButton	
	 */
	private JButton getB_stop() {
		if (b_stop == null) {
			b_stop = new JButton();
			b_stop.setText("Stop");
			b_stop.setPreferredSize(new Dimension(100, 25));
		}
		return b_stop;
	}

	/**
	 * This method initializes jPanel1	
	 * 	
	 * @return javax.swing.JPanel	
	 */
	private JPanel getJPanel1() {
		if (jPanel1 == null) {
			jPanel1 = new JPanel();
			jPanel1.setLayout(new BoxLayout(getJPanel1(), BoxLayout.X_AXIS));
			jPanel1.setPreferredSize(new Dimension(160, 200));
			jPanel1.setComponentOrientation(ComponentOrientation.UNKNOWN);
			jPanel1.add(Box.createHorizontalStrut(10));
			jPanel1.add(getJPanel5(), null);
		}
		return jPanel1;
	}
	
	/**
	 * This method initializes l_userlist	
	 * 	
	 * @return javax.swing.JList	
	 */
	private JList getL_userlist() {
		if (l_userlist == null) {
			l_userlist = new JList(this.getUserList());
		}
		return l_userlist;
	}
	
	private DefaultListModel getUserList(){
		if(userList == null){
			userList=new DefaultListModel();	
		}
		return userList;
	}

	/**
	 * This method initializes l_msglist	
	 * 	
	 * @return javax.swing.JList	
	 */
	private JList getL_msglist() {
		if (l_msglist == null) {
			l_msglist = new JList();
			l_msglist.setModel(getMsglist());
		}
		return l_msglist;
	}

	/**
	 * This method initializes jScrollPane	
	 * 	
	 * @return javax.swing.JScrollPane	
	 */
	private JScrollPane getJScrollPane() {
		if (jScrollPane == null) {
			jScrollPane = new JScrollPane();
			jScrollPane.setPreferredSize(new Dimension(150, 0));
			jScrollPane.setBorder(BorderFactory.createEtchedBorder(EtchedBorder.LOWERED));
			jScrollPane.setViewportView(getL_userlist());
		}
		return jScrollPane;
	}

	/**
	 * This method initializes jPanel4	
	 * 	
	 * @return javax.swing.JPanel	
	 */
	private JPanel getJPanel4() {
		if (jPanel4 == null) {
			FlowLayout flowLayout1 = new FlowLayout();
			flowLayout1.setAlignment(FlowLayout.LEFT);
			jLabel2 = new JLabel();
			jLabel2.setText("User Online:");
			jPanel4 = new JPanel();
			jPanel4.setLayout(flowLayout1);
			jPanel4.setPreferredSize(new Dimension(150, 25));
			jPanel4.setMaximumSize(new Dimension(150, 25));
			jPanel4.add(jLabel2, null);
		}
		return jPanel4;
	}

	/**
	 * This method initializes jSend	
	 * 	
	 * @return javax.swing.JButton	
	 */
	private JButton getJSend() {
		if (jSend == null) {
			jSend = new JButton();
			jSend.setText("Send");
		}
		return jSend;
	}

	/**
	 * This method initializes jExit	
	 * 	
	 * @return javax.swing.JButton	
	 */
	private JButton getJExit() {
		if (jExit == null) {
			jExit = new JButton();
			jExit.setText("Exit");
			jExit.setPreferredSize(new Dimension(70, 25));
		}
		return jExit;
	}

	/**
	 * This method initializes jPanel5	
	 * 	
	 * @return javax.swing.JPanel	
	 */
	private JPanel getJPanel5() {
		if (jPanel5 == null) {
			jPanel5 = new JPanel();
			jPanel5.setLayout(new BoxLayout(getJPanel5(), BoxLayout.Y_AXIS));
			jPanel5.setPreferredSize(new Dimension(160, 25));
			jPanel5.add(getJPanel4(), null);
			jPanel5.add(getJScrollPane(), null);
		}
		return jPanel5;
	}

	/**
	 * This method initializes msglist	
	 * 	
	 * @return javax.swing.DefaultListModel	
	 */
	private DefaultListModel getMsglist() {
		if (msglist == null) {
			msglist = new DefaultListModel();
		}
		return msglist;
	}

	/**
	 * This method initializes jScrollPane1	
	 * 	
	 * @return javax.swing.JScrollPane	
	 */
	private JScrollPane getJScrollPane1() {
		if (jScrollPane1 == null) {
			jScrollPane1 = new JScrollPane();
			jScrollPane1.setBorder(BorderFactory.createEtchedBorder(EtchedBorder.LOWERED));
			jScrollPane1.setViewportView(getL_msglist());
		}
		return jScrollPane1;
	}

	/**
	 * This method initializes jPanel2	
	 * 	
	 * @return javax.swing.JPanel	
	 */
	private JPanel getJPanel2() {
		if (jPanel2 == null) {
			FlowLayout flowLayout3 = new FlowLayout();
			flowLayout3.setAlignment(FlowLayout.RIGHT);
			jPanel2 = new JPanel();
			jPanel2.setLayout(flowLayout3);
			jPanel2.add(getTx_msg(), null);
			jPanel2.add(getJSend(), null);
			jPanel2.add(getJExit(), null);
		}
		return jPanel2;
	}

	/**
	 * This method initializes tx_msg	
	 * 	
	 * @return javax.swing.JTextField	
	 */
	private JTextField getTx_msg() {
		if (tx_msg == null) {
			tx_msg = new JTextField();
			tx_msg.setPreferredSize(new Dimension(380, 19));
		}
		return tx_msg;
	}

}  //  @jve:decl-index=0:visual-constraint="10,10"
