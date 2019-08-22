"""Tests for the :mod:`campy.datastructures.pqueue` module."""
# import priorityQueue as PriorityQueue
import pqueue as PriorityQueue

def test_create_empty_queue():
    pq = PriorityQueue.PriorityQueue()
    assert pq.is_empty()

    print("test_create_empty_queue: passed")


def test_basic_operations():
    pq = PriorityQueue.PriorityQueue()

    pq.enqueue(8, 'Sam')
    pq.enqueue(6, 'Tristen')
    pq.dequeue() == (6, 'Tristen')
    assert pq.peek() == (8, 'Sam')

    pq.enqueue(1, 'of one')
    assert str(pq) == "[[1, 'of one'], [8, 'Sam']]"
    pq2 = PriorityQueue.PriorityQueue()
    pq2.enqueue(8, 'Sam')
    pq2.enqueue(1, 'of one')
    assert pq == pq2

    pq2.clear()
    assert pq2.is_empty()

    print("test_basic_operations: passed")

if __name__ == '__main__':
	test_create_empty_queue()
	test_basic_operations()