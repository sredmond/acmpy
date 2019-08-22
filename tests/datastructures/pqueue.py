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
        #keep track of entries for updating and other tasks
        self.entries = {} 
        #initialize heap
        self._heap = [] 
        _heapq.heapify(self._heap)

    def add(self, priority, value):
        '''add a new value or updae the priority'''

        #check if the value being added already exists in the queue and if it does then remove it
        if value in self.entries:
            self.remove(value)

        #add the entry
        new_entry = [priority, value]
        self.entries[value] = new_entry
        _heapq.heappush(self._heap, new_entry)

    def back(self):
        return self._heap[-1]

    def change_priority(self, value, new_priority):
        #since our add function already takes care of this, just call that instead
        self.add(value, new_priority)
                
    #Initializes a new empty heap to replace the old one
    def clear(self):
        self._heap = []


    def remove(self, value):
        '''keep heap invariance by marking as removed'''
        entry = self.entries[value]
        entry[-1] = PriorityQueue._REMOVED
        pass

    #return the front most element aka highest priority
    def front(self):
        '''since we are marking things as removed to keep the heap invariance, we must 
        check if the front element needs to be removed. If it is marked as removed, we pop it and and delete it from the entries
        if it is we continue to keep the heap structure'''
        while self._heap:
            priority, task = _heapq.heappop(self._heap)
            if task is not PriorityQueue._REMOVED:
                del self.entries[task]
                return priority, task
        raise KeyError("The priority queue is empty")

    def __len__(self):
        #return len of entries because that is the working list of everything in the heap, but doesnt include the priorities or anything
        return len(self.entries)

    def __eq__(self, other):
        return self._heap == other._heap

    def peek(self):
        '''uses a variable to temp store the value and return it without using heappop'''
        priority, value = self._heap[0]
        return priority, value

    def peek_value(self):
        '''unloads the priority and value but only returns the value'''
        priority, value = self._heap[0]
        return value

    def peek_priority(self):
        '''unloads priority and value buut only returns priority'''
        priority, value = self._heap[0]
        return priority

    def is_empty(self):
        '''if the heap is empty it will appear as an empty list'''
        if self._heap == []:
            return True

    def __str__(self):
        temp = [str(e) for e in self._heap if e[-1] is not PriorityQueue._REMOVED]
        return "[%s]" % ", ".join(temp)

    enqueue = add
    dequeue = front


