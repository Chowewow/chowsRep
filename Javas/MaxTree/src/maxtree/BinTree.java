/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package maxtree;

import CITS2200.BinaryTree;
import CITS2200.Iterator;
import CITS2200.OutOfBounds;
import java.util.LinkedList;

public class BinTree<E> extends BinaryTree<E> {

	public BinTree() {
		super();
	}

	public BinTree(E item, BinaryTree<E> ltree, BinaryTree<E> rtree) {
		super(item, ltree, rtree);
	}

	@SuppressWarnings("unchecked")
	public boolean equals(Object o) {
		// TODO: Implement equals
		if (!(o instanceof BinTree) || o == null) {
			return false;
		}

		BinTree<E> otherTree = (BinTree<E>) o;

		if (isEmpty() && otherTree.isEmpty()) {
			return true;
		}

		E e1 = getItem();
		E e2 = otherTree.getItem();

		if (e1 == null && e2 != null) {
			return false;
		}
		if (e1 != null && e2 == null) {
			return false;
		}

		if (e1 != null && e2 != null && e1 != e2) {
			if (!e1.equals(e2)) {
				return false;
			}
		}

		BinTree<E> ourLeftTree = (BinTree<E>) getLeft();
		BinTree<E> ourRightTree = (BinTree<E>) getRight();
		BinTree<E> theirLeftTree = (BinTree<E>) otherTree.getLeft();
		BinTree<E> theirRightTree = (BinTree<E>) otherTree.getRight();

		return ourLeftTree.equals(theirLeftTree) && ourRightTree.equals(theirRightTree);
	}

	class QueueIterator<E> implements Iterator<E> {

		LinkedList<E> queue;

		public QueueIterator(BinTree<E> tree) {
			queue = new LinkedList<E>();
			LinkedList<BinTree<E>> binTreeQueue = new LinkedList<BinTree<E>>();
			binTreeQueue.addLast(tree);
			while (!binTreeQueue.isEmpty()) {
				BinTree<E> current = binTreeQueue.pop();

				if (current.isEmpty()) {
					continue;
				}

				queue.addLast(current.getItem());
				binTreeQueue.addLast((BinTree<E>) current.getLeft());
				binTreeQueue.addLast((BinTree<E>) current.getRight());
			}
		}

		@Override
		public boolean hasNext() {
// TODO Auto-generated method stub
			return !queue.isEmpty();
		}

		@Override
		public E next() throws OutOfBounds {
// TODO Auto-generated method stub
			if (queue.isEmpty()) {
				throw new OutOfBounds("Iterator has no more elements!");
			}

			return queue.pop();
		}

	}

	public Iterator<E> iterator() {
		QueueIterator<E> it = new QueueIterator<E>(this);
		return it;
	}

	public static void main(String[] args) {
		// TODO code application logic here
		BinTree myTree = new BinTree();
		
		

	}
}
