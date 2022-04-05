/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package lock;

/**
 *
 * @author chow
 */
public interface Lock {

	public boolean open(int code);

	public boolean close();

	public boolean changeCode(int code, int newCode);

	/**
	 *
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO code application logic here
		Lock myLock;
		myLock = new LockString(669, false);
		myLock.open(669);
		myLock.changeCode(669, 666);
		myLock.open(669);
		myLock.close();
		myLock.open(669);
	}
}

/**
 *
 * @author chow
 */
class LockInt implements Lock {

	private int code;

	private boolean isOpen;

	/**
	 *
	 * @param code
	 * @return
	 */
	@Override
	public boolean open(int code) {
		if (code == this.code && isOpen == false) {
			isOpen = true;
			System.out.println("Hey, I'm in.");
			return isOpen;

		} else if (isOpen == true) {
			System.out.println("Already Open.");
			return false;
		} else {
			System.out.println("Wrong code brah.");
			return false;
		}
	}

	/**
	 *
	 * @return
	 */
	@Override
	public boolean close() {
		if (isOpen == true) {
			isOpen = false;
			System.out.println("Successfully closed!");
			return true;
		} else {
			System.out.println("Already locked.");
			return false;
		}

	}

	/**
	 *
	 * @param code
	 * @param newCode
	 * @return
	 */
	@Override
	public boolean changeCode(int code, int newCode) {
		if (code == this.code) {
			this.code = newCode;
			System.out.println("Code successfully changed!");
			return true;
		} else {
			System.out.println("Wrong code.");
			return false;
		}
	}

	/**
	 *
	 * @param code
	 * @param isOpen
	 */
	public LockInt(int code, boolean isOpen) {
		this.code = code;
		this.isOpen = isOpen;
	}

}

class LockString implements Lock {

	private String code;
	private boolean isOpen;

	/**
	 *
	 * @param code
	 * @return
	 */
	@Override
	public boolean open(int code) {
		if (code == Integer.parseInt(this.code) && isOpen == false) {
			isOpen = true;
			System.out.println("Hey, I'm in.");
			return isOpen;

		} else if (isOpen == true) {
			System.out.println("Already Open.");
			return false;
		} else {
			System.out.println("Wrong code brah.");
			return false;
		}
	}

	/**
	 *
	 * @return
	 */
	@Override
	public boolean close() {
		if (isOpen == true) {
			isOpen = false;
			System.out.println("Successfully closed!");
			return true;
		} else {
			System.out.println("Already locked.");
			return false;
		}

	}

	/**
	 *
	 * @param code
	 * @param newCode
	 * @return
	 */
	@Override
	public boolean changeCode(int code, int newCode) {
		if (code == Integer.parseInt(this.code) && Integer.toString(newCode).length() == 3) {
			this.code = Integer.toString(newCode);
			System.out.println("Code successfully changed!");
			return true;
		} else {
			System.out.println("Wrong code.");
			return false;
		}
	}
	/**
	 * Constructor
	 * @param code
	 * @param isOpen 
	 */
	public LockString(int code, boolean isOpen) {
		if (Integer.toString(code).length() == 3) {
			this.code = Integer.toString(code);
			this.isOpen = isOpen;
		} else {
			throw new NumberFormatException("Enter a valid code");
		}

	}
}
