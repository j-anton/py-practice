
class Array(object):
    
    def __init__(self, size, default = None):
        
        self.size = size
        self.items = list()
        self.type = type

        if (type == None):
            print('Array requires a type')

        if (default == None):
            for i in range(size):
                self.items.append(default)

        else: 
            # Verify that the default array is an allowed size
            if (len(default) > size):
                print ('Array elements exceed array size')

            else:
                # Fill the default values
                for j in range(0,len(default)):
                    self.items.append(default[j])

                # Everything that is not defaulted is None 
                for i in range(len(default),size):
                    self.items.append(None)


    def printarr(self):
        for i in range(0, self.arrlen()):
            print (self.items[i])


    def arrlen(self):
        length = 0
        for i in self.items:

            if i == None:
                continue

            else:
                length += 1

        return length


    def insertfront(self, elem):
        # Verify there is enough room
        if (self.arrlen() >= self.size):
            print ('Array index out of range')
        
        #Shift all elements back and insert at front
        else:
            for i in range(self.arrlen(), 0, -1):
                self.items[i]=self.items[i-1]
            self.items[0]=elem


    def insertlast(self, elem):
        #verify there is enough room 
        if (self.arrlen() >= self.size):
            print('Array index out of range')

        #Insert new element at back
        else: 
            self.items[self.arrlen()]=elem


    def insertat(self, elem, index):
        #verify there is enough room
        if (self.arrlen()>=self.size):
            print('Array index out of range')
        
        #insert at desired index
        else:
            for i in range(self.arrlen(), index, -1):
                self.items[i] = self.items[i-1]
            self.items[index] = elem


    def insertafter(self, elem, index):
        # verify there is enough room
        if (self.arrlen()>=self.size):
            print('Array index out of range')

        #Insert element after index
        else:
            for i in range(self.arrlen(), index+1, -1):
                self.items[i] = self.items[i-1]
            self.items[index+1] = elem


    def insertbefore(self, elem, index):
        #verify there is enough room
        if (self.arrlen()>=self.size):
            print('Array index out of range')
        
        #Insert element before index
        else:
            for i in range(self.arrlen(), index-1, -1):
                self.items[i] = self.items[i-1]
            self.items[index-1] = elem


    def delelem(self, elem):
        #verify the element is in the array
        if elem not in self.items:
            print('Element not present in array')
        
        #Delete first occurance of element, shift items up
        else:
            index = self.items.index(elem)
            print(index, 'index')
            for i in range(index,self.arrlen()-1, 1):
                self.items[i] = self.items[i+1]
            self.items[self.arrlen()-1]=None

    def searcharr(self, elem):
        if elem not in self.items:
            print('Element not present in array')
        
        else:
            index = 0
            for i in range(self.arrlen()):
                if(self.items[i] == elem):
                    break
                else:
                    index +=1
            
            print (elem,'at index',index,'in array.')