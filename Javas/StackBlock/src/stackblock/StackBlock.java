/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package stackblock;

import CITS2200.Stack;
import CITS2200.Underflow;
import CITS2200.Overflow;

/**
 *
 * @author chow
 */
public class StackBlock implements Stack {

	private Object[] item;
	private int first;

	public StackBlock(int size) {
		first = 0;
		item = new Object[size];
	}

	/**
	 * 
	 * @returns true if array is empty
	 */
	@Override
	public boolean isEmpty() {
		return first == 0 && item[first] == null;
	}
	/**
	 * 
	 * @returns true if array is full
	 */
	public boolean isFull() {
		return first == item.length;
	}

	/**
	 *
	 * @param item is pushed onto stack
	 * @throws Overflow
	 */
	@Override
	public void push(Object item) throws Overflow {
		if (!isFull()) {
			this.item[first] = item;
			first++;
		} else {
			throw new Overflow("Stack Overflow");
		}

	}

	/**
	 *
	 * @returns the top item of the stack
	 * @throws Underflow
	 */
	@Override
	public Object examine() throws Underflow {
		if (!isEmpty()) {
			return item[first - 1];
		} else {
			throw new Underflow("Examining empty stack");
		}

	}

	/**
	 *
	 * @return the top item of the stack and removes it
	 * @throws Underflow
	 */
	@Override
	public Object pop() throws Underflow {
		if (!isEmpty()) {
			Object popped = item[first - 1];
			item[first - 1] = null;
			first--;
			return popped;
		} else {
			throw new Underflow("Cannot delete from an empty stack");
		}

	}

	/**
	 * @param args the command line arguments
	 */
	public static void main(String[] args) {
		// TODO code application logic here
		Stack stacks = new StackBlock(4);
		System.out.println(stacks.examine());
		
		System.out.println();
	}

}


