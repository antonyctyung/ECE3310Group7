# ECE 3310 Group 7 Report 2 Question 5 
# Author: Choi Tim Antony Yung

class LinkedListNode:
    def __init__(self,data,next=None):
        self._data = data
        self._next = next

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self,data):
        self._data = data

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self,next):
        self._next = next

    def __str__(self):
        return self._data.__str__()

class DoublyLinkedListNode(LinkedListNode):
    def __init__(self,data,next=None,prev=None):
        super.__init__(self,data,next)
        self._prev = prev
    
    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prev):
        self._prev = prev

class LinkedList:
    def __init__(self):
        self._firstNode = None
        self._lastNode = None

    @property
    def firstNode(self):
        return self._firstNode
    
    @firstNode.setter
    def firstNode(self, firstNode):
        self._firstNode = firstNode

    @property
    def lastNode(self):
        return self._lastNode
    
    @lastNode.setter
    def lastNode(self, lastNode):
        self._lastNode = lastNode

    def isEmpty(self):
        return self._firstNode == None
    
    def InsertAtFront(self,insertItem):
        if self.isEmpty():
            self._firstNode = LinkedListNode(insertItem)
            self._lastNode = self._firstNode
        else:
            newNode = LinkedListNode(insertItem,self._firstNode)
            self._firstNode = newNode

    def InsertAtBack(self,insertItem):
        if self.isEmpty():
            self._firstNode = LinkedListNode(insertItem)
            self._lastNode = self._firstNode
        else:
            newNode = LinkedListNode(insertItem)
            self._lastNode.next = newNode
            self._lastNode = newNode
            
    def RemoveFromFront(self):
        if self.isEmpty():
            raise IndexError('Attempting to remove from an empty list.')

        removeItem = self._firstNode.data

        if self._firstNode is self._lastNode:
            self._firstNode = None
            self._lastNode = None
        else:
            newfirst = self._firstNode.next
            self._firstNode = newfirst

        return removeItem

    def RemoveFromBack(self):
        if self.isEmpty():
            raise IndexError('Attempting to remove from an empty list.')
            
        removeItem = self._lastNode.data

        if self._firstNode is self._lastNode:
            self._firstNode = None
            self._lastNode = None
        else:
            current = self._firstNode
            while current.next is not self._lastNode:
                nextNode = current.next
                current = nextNode
            
            self._lastNode = current
            current.next = None
        return removeItem

    def InsertInTheMiddle(self, insertItem, idx):
        if idx <= 0:
            self.InsertAtFront(insertItem)
            return
        else:
            current = self._firstNode
            while idx > 1:
                if (current is self.)
                nextNode = current.next
                current = nextNode
                idx = idx - 1
            # variable current is now the one before the one at idx
            if current is self._lastNode:
                self.InsertAtBack(insertItem)
                return
            else:
                newNode = LinkedListNode(insertItem,current.next)
                current.next = newNode
        return

            