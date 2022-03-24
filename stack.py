
class Node(object):
    
    def __init__(self, data):
        self._data = data
        self._next = None


class Stack(object):
    
    def __init__(self):
        self._top = None

    def __str__(self):
        string = ''
        ptr = self._top
        while (ptr != None):
            string += str(ptr._data)+' '
            ptr = ptr._next
        return string

    def push(self, data):
        node = Node(data)
        node._next = self._top
        self._top = node

    def pop(self):
        if (self._top == None):
            raise Exception('Empty Stack')
        node = self._top
        self._top = self._top._next
        return node._data

    def peek(self):
        if (self._top == None):
            raise Exception('Empty Stack')
        return self._top._data

    def  isEmpty(self):
        return self._top == None

stack = Stack()
stack.push(22)
stack.push(33)
print(stack.isEmpty())
print(stack.peek())
print (stack)