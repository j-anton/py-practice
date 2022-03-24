
class Node(object):
    
    def __init__(self, data):
        self._data = data
        self._next = None


class Queue(object):
    
    def __init__(self):
        self._first = None
        self._last = None

    def __str__(self):
        string = ''
        ptr = self._first
        while (ptr != None):
            string += str(ptr._data)+' '
            ptr = ptr._next
        return string

    def add(self, data):
        node = Node(data) 
        if (self._first == None): 
            self._first = node
        if (self._last != None):
            self._last._next = node
        self._last = node

    def remove(self):
        if (self._first == None):
            raise Exception('Empty Queue')
        data = self._first._data
        self._first = self._first._next
        if self._first == None: 
            self._last = None
        return data

    def peek(self):
        if (self._first == None):
            raise Exception('Empty Stack')
        return self._first._data

    def  isEmpty(self):
        return self._first == None

queue = Queue()
queue.add(22)
queue.add(33)
queue.add(44)
print(queue.remove())
print(queue.isEmpty())
print(queue.peek())
print (queue)