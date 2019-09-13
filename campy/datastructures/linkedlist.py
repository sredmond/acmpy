"""

"""

class LinkedList(object):
    def __init__(self, head = None):
        self.head = head
        self.length = 0

    def __len__(self):
        return self.length

    def __getitem__(self, position):
        #catch index error first
        if position >= len(self) or position < 0:
            raise IndexError("Index out of range")

        '''traverse to the position passed, using xrange for memory efficiency. 
        range() would be better if looping over the range repeatedly but we are not'''
        curr = self.head
        for node in range(position):
            curr = curr.next

        return curr

    # Do we even need a __setitem__ for the linked list?
    def __setitem__(self, position, value):
        if position < 0 or position >= len(self):
            raise IndexError("Index out of range")

        curr = self.head
        for node in range(position):
            curr = curr.next

        curr.value = value
        return 

    def __delitem__(self, position):
        '''raises an index error if the position is out of the 
        list's range. Removes in O(n)'''
        if position >= len(self) or position < 0:
            raise IndexError("Index out of range")
        elif position == 0:
            self.head = self.head.next

        #get the node we want to delete
        curr_node = self[position]
        #get the node before the one to delete
        prev_node = self[position - 1]
        #set the next value to point to the node after the one we want to delete
        prev_node.next = curr_node.next
        #cut the deleted node from its next node
        curr_node.next = None
        #decrease length attribute by one
        self.length -= 1


    def __iter__(self):
        '''define an iter function for faster iteration over the list
        a combination of len and getitem would be O(n^2) for iteration, but with 
        this function it can be much more efficient. Random access can still use other methods'''
        curr = self.head

        while curr:
            yield curr
            curr = curr.next

    # def check_position(self, position):
    #     '''might use this to consolidate later and remove all the repetitive index error checks'''
    #     if position >= len(self) or position < 0:
    #         raise IndexError("Index out of range")

    def equals(self, list2):
        '''compare two lists and return true if both lists have 
        the same values in the same order as each other'''
        if len(self) != len(list2):
            return False
        for node_self, node_list2 in zip(self, list2):
            if node_self.value != node_list2.value:
                return False
        return True

    def insert(self, position, value):
        '''inserts a node to the left of the specified value. If the index provided
        is 1, then the new node will be placed before 1, and all nodes after will be moved to the 
        right.'''

        if position >= len(self) or position < 0:
            raise IndexError("Index out of range")
        #special case if inserting at the front of the list
        elif position == 0:
            new_node = LinkedListNode(value)
            new_node.next = self.head
            self.head = new_node
            
        else:
            new_node = LinkedListNode(value)
            #get position of node and one before it
            next_node = self[position]
            prev_node = self[position - 1]
            #point new_node to the one coming to the right of it
            new_node.next = next_node
            #change reference of prev_node from the old to the new_node
            prev_node.next = new_node

        #update length
        self.length += 1

    def add(self, value):
        '''add node to the end of the list'''
        new_node = LinkedListNode(value)

        if self.length == 0:
            self.head = new_node
            self.length += 1
        #create node and get the node at the end of the list
        else:
            end_node = self[len(self) - 1]
            #set reference of ending node to the new node
            end_node.next = new_node

            #update length
            self.length += 1

    def get(self, position):
        '''method that returns the element at the specified index'''
        return self[position]

    def isEmpty(self):
        '''return whether the list is empty or not. The list is empty when he length is 0, 
        but to ensure that no miscounting can mess it up the head must also be None'''
        if self.length == 0 and self.head == None:
            return True
        return False

    def remove(self, position):
        '''remove item at specified index'''
        if position >= len(self) or position < 0:
            raise IndexError("Index out of range.")

        del self[position]

    def set(self, position, value):
        if position >= len(self) or position < 0:
            raise IndexError("Index out of range.")

        self[position] = value

    def size(self):
        '''method to return how many elements are in the list'''
        return len(self)

class LinkedListNode(object):
    '''use slots to save on memory when creating nodes since
    we know what values to expect when creating a node'''
    __slots__ = ('value', 'next')

    def __init__(self, value, next_node = None):
        self.value = value
        self.next = next_node

    def __str__(self):
        return "LLNode(value={self.value})".format(self=self)
