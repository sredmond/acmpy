# TODO(sredmond): Possibly rename this file priorityqueue.h for compatibility.
"""
Min-heap.
"""
import collections as _collections

# TODO(sredmond): Make this into a collection subclass.
# TODO(sredmond): Use namedtuples.
import heapq as _heapq
import itertools

class PriorityQueue(object):

    _REMOVED = "<REMOVED>"

    def __init__(self):
        self.entries = {} #keep track of entries for updating and other tasks
        self._heap = []
        _heapq.heapify(self._heap)

    def add(self, priority, value):
        '''add a new value or updae the priority'''
        if value in self.entries:
            self.remove(value)


        new_entry = [priority, value]
        self.entries[value] = new_entry
        _heapq.heappush(self._heap, new_entry)

    def back(self):
        return self._heap[-1]

    def change_priority(self, value, new_priority):
        self.add(value, new_priority)
                

    def clear(self):
        self._heap = []

    def remove(self, value):
        '''keep heap invariance by marking as removed'''
        entry = self.entries[value]
        entry[-1] = PriorityQueue._REMOVED
        pass

    def front(self):

        while self._heap:
            priority, task = _heapq.heappop(self._heap)
            if task is not PriorityQueue._REMOVED:
                del self.entries[task]
                return priority, task
        raise KeyError("The priority queue is empty")

    def __len__(self):
        return len(self.entries)

    def __eq__(self, other):
        return self._heap == other._heap

    def peek(self):
        priority, value = self._heap[0]
        return priority, value

    def peek_value(self):
        priority, value = self._heap[0]
        return value

    def peek_priority(self):
        priority, value = self._heap[0]
        return priority

    def is_empty(self):
        if self._heap == []:
            return True

    def __str__(self):
        temp = [str(e) for e in self._heap if e[-1] is not PriorityQueue._REMOVED]
        return "[%s]" % ", ".join(temp)

    enqueue = add
    dequeue = front


