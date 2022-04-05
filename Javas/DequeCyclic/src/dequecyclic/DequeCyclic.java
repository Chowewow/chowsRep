
import CITS2200.Deque;
import CITS2200.Overflow;
import CITS2200.Underflow;

@SuppressWarnings("unchecked")

public class DequeCyclic<E> implements Deque<E> {

	// TODO: Add any member variables you need
	private E[] items;
	private int first;
	private int last;

	public DequeCyclic(int size) {
		// TODO: Construct empty DequeCyclic of given size
		items = (E[]) new Object[size + 1];
		first = -1;
		last = -1;

	}

	public boolean isEmpty() {
		// TODO: Implement isEmpty()
		return first == -1 && last == -1;
	}

	public boolean isFull() {
		// TODO: Implement isFull()
		return first == (last + 2) % items.length;
	}

	public void pushLeft(E item) throws Overflow {
		// TODO: Implement pushLeft()
		if (!isFull()) {
			last = (last + 1) % items.length;
			items[last] = item;

		} else if (isEmpty()) {
			first = 0;
			last = 0;
			items[last] = item;
		} else {
			throw new Overflow("enqueing to full queue");
		}

	}

	public void pushRight(E item) throws Overflow {
		// TODO: Implement pushRight()
		if (!isFull()) {
			if (first > 0) {
				first = (first - 1) % items.length;
				items[first] = item;

			} else {
				first = items.length - 1;
				items[first] = item;
			}
		} else if (isEmpty()) {
			first = 0;
			last = 0;
			items[first] = item;

		} else {
			throw new Overflow("Queue is full");
		}
	}

	public E peekLeft() throws Underflow {
		// TODO: Implement peekLeft()
		if (!isEmpty()) {
			return (E) items[last];
		} else {
			throw new Underflow("Examining an empty queue");
		}
	}

	public E peekRight() throws Underflow {
		// TODO: Implement peekRight()
		if (!isEmpty()) {
			return items[first];
		} else {
			throw new Underflow("Examining an empty queue");
		}
	}

	public E popLeft() throws Underflow {
		// TODO: Implement popLeft()
		if (!isEmpty()) {
			if (last > 0) {
				Object temp = items[last];
				items[last] = null;
				last--;
				if (items[last] == null) {
					last = -1;
				}

				return (E) temp;
			} else {
				Object temp = items[last];
				items[last] = null;
				last = items.length - 1;
				if (items[last] == null) {
					last = -1;
					first = -1;
				}
				return (E) temp;
			}
		} else {
			throw new Underflow("Queue is empty");
		}
	}

	public E popRight() throws Underflow {
		// TODO: Implement popRight()
		if (!isEmpty()) 
		{
			Object temp;

			temp = items[first];
			items[first] = null;
			first = (first + 1) % items.length;
			if (items[first] == null) {
				first = -1;
				last = -1;
			}
			return (E) temp;
		} else {
			throw new Underflow("Queue is empty");
		}
	}
}
