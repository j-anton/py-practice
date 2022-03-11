

class Node(object):

    def __init__(self, value=None):
        self.next = None
        self.prior = None
        self.value = value

class LList(object):
    
    def __init__(self, value = None):
        self.head = None
        self.tail = None

        if value != None:
            new_node = Node(value)
            self.head = self.tail = new_node 

    def printllistf(self):
        ptr = self.head
        while (ptr != None):
            print(ptr.value)
            ptr = ptr.next

    def printllistb(self):
        ptr = self.tail
        while(ptr != None):
            print(ptr.value)
            ptr = ptr.prior

    def append(self, value):
        if self.head == None:
            tmp = Node(value)
            self.head = self.tail = tmp
        else:
            new_node = Node(value)
            prev_tail = self.tail
            prev_tail.next = self.tail = new_node
            new_node.prior = prev_tail

    def insert(self, value, index):
        ptr = self.head
        for i in range (0, index, 1):
            if (i == index-2):
                if ptr == None: 
                    self.append(value)
                    return
                else:
                    new_node = Node(value)
                    new_node.next = ptr.next
                    ptr.next = new_node
                    new_node.next.prior = new_node
                    new_node.prior = ptr
                    return
            else:
                if ptr == None: 
                    print ('Not enough elements in list for insert')
                    return
                else: 
                    ptr = ptr.next

    def delete(self, index):
        ptr = self.head
        for i in range (1, index, 1):
            if (ptr == None): 
                print('Not enough elements in list for delete')
            ptr = ptr.next
        
        # Only element in linked list
        if ptr.next == None and ptr.prior == None:
            self.head = self.tail = None
        
        # Deleted element is Tail
        elif ptr.next == None:
            self.tail = ptr.prior
            ptr.prior.next = None
        
        # Deleted element is Head
        elif ptr.prior == None: 
            self.head = ptr.next
            ptr.next.prior = None
        
        #Other cases
        else: 
            ptr.prior.next = ptr.next
            ptr.next.prior = ptr.prior

    def rmvalue(self, value):
        ptr = self.head
        while (ptr != None):
            if (ptr.value == value):

                # Only element in linked list
                if ptr.next == None and ptr.prior == None: 
                    self.head = self.tail = None

                # Deleted element is Tail
                elif ptr.next == None: 
                    self.tail = ptr.prior
                    ptr.prior.next = None

                # Deleted element is Head
                elif ptr.prior == None: 
                    self.head = ptr.next
                    ptr.next.prior = None

                #Other cases
                else:
                    ptr.prior.next = ptr.next
                    ptr.next.prior = ptr.prior
            ptr = ptr.next
