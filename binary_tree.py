
class Node (object):
    
    def __init__(self, data):
        self.data = data
        self.count = 1
        self.left = None
        self.right = None 

    @classmethod
    def from_list(cls, data: list):
        print('DEBUG: ADD THIS FUNCTIONALITY')

    def dump(self):#,#string):
        if self == None: 
            print('no tree')
        
        if self.left != None:
            self.left.dump()
    
        print(self.data)
        
        if self.right != None:
            self.right.dump()


    def insert(self, data):

        if (self.data == None):
            print ('root none')
            self.data = data

        elif (self.data == data):
            print(self.data, '==', data)
            self.count += 1

        elif (self.data > data):
            print(self.data, '>', data)
            if (self.left == None): 
                self.left = Node(data)
                print('inserted if', self.data, data)
            else: 
                self.left.insert(data)
                print('inserted else', self.data, data)

        elif (self.data < data):
            print(self.data, '<', data)
            if (self.right == None): 
                self.right = Node(data)
                print('inserted', data)
            else: 
                self.right.insert(data)
                print('inserted', self.data, data)

        #data == parent node
        # data < parent node
        # data > parent node

tree = Node(10)
tree.insert(11)
tree.insert(5)
tree.insert(4)
print (tree.dump())