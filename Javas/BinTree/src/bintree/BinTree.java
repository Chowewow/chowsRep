/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package bintree;

import java.util.LinkedList;
import CITS2200.BinaryTree;
import CITS2200.Iterator;
import CITS2200.OutOfBounds;

@SuppressWarnings("unchecked")


public class BinTree<E> extends BinaryTree<E> {

	public BinTree() {
		super();
	}

	public BinTree(E item, BinaryTree<E> ltree, BinaryTree<E> rtree) {
		super(item, ltree, rtree);

	}

	public boolean equals(Object o) {
		// TODO: Implement equals
		if (!(o == null || o instanceof BinTree)) {
			return false;
		}
		BinTree<E> inputTree = (BinTree<E>) o;
		if (isEmpty() && inputTree.isEmpty()) {
			return true;
		}

		E treeItem = getItem();
		E inputTreeItem = inputTree.getItem();

		if (inputTreeItem != null && treeItem == null) {
			return false;
		} else if (inputTreeItem == null && treeItem != null) {
			return false;
		} else if (treeItem != null && inputTreeItem != null && treeItem != inputTreeItem) {
			if (!treeItem.equals(inputTreeItem)) {
				return false;
			}
		}
		BinTree<E> leftTree = (BinTree<E>) getLeft();
		BinTree<E> rightTree = (BinTree<E>) getRight();
		BinTree<E> inputLeftTree = (BinTree<E>) inputTree.getLeft();
		BinTree<E> inputRightTree = (BinTree<E>) inputTree.getRight();

		return leftTree.equals(inputLeftTree) && rightTree.equals(inputRightTree);
	}

	public Iterator<E> iterator() {
		// TODO: Implement iterator
		// NOTE: You may need to create an inner class to implement the iterator
		return new BinTreeIterator<>(this);
	}

	private class BinTreeIterator<E> implements Iterator<E> {

		LinkedList<E> queue;

		public BinTreeIterator(BinTree<E> tree) {
			queue = new LinkedList<>();
			LinkedList<BinTree<E>> binTreeQueue = new LinkedList<>();
			binTreeQueue.addLast(tree);
			while (!binTreeQueue.isEmpty()) {
				BinTree<E> curTree = binTreeQueue.pop();
				if (curTree.isEmpty()) {
					continue;
				}

				queue.addLast(curTree.getItem());
				binTreeQueue.addLast((BinTree<E>) curTree.getLeft());
				binTreeQueue.addLast((BinTree<E>) curTree.getRight());
			}
		}

		@Override
		public boolean hasNext() {
			return !queue.isEmpty();
		}

		@Override
		public E next() throws OutOfBounds {
			if (queue.isEmpty()) {
				throw new OutOfBounds("Queue is Empty");
			}
			return queue.pop();
		}
	}

	/**
	 * @param args the command line arguments
	 */
	public static void main(String[] args) {
		// TODO code application logic here
		BinTree myTree = new BinTree();
		System.out.println(myTree.toString());

	}
}
