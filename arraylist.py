
class ArrayList(object): 

    def __init__(self, size = 1):
        self.max = size
        self.list = [None]*self.max
        self.size = 0

    def __str__(self):
        string = 'ArrayList size:'+str(self.size)+'/'+str(self.max)+'.\n'
        for elem in self.list: 
            string += str(elem)+' '
        return string

    def _doublelist(self):
        new_list = self.list + [None]*self.max
        self.list = new_list
        self.max *= 2

    def push(self, value):
        if self.size >= self.max:
            #double array size
            self._doublelist()
        self.list[self.size] = value
        self.size += 1

    def merge(self, arrlist1, arrlist2):
        self.list = [None]*(arrlist1.max+arrlist2.max)
        for i in range(0,arrlist1.size):
            self.push(arrlist1.list[i])
        for i in range(0,arrlist2.size):
            self.push(arrlist2.list[i])
        self.max = (arrlist1.max + arrlist2.max)*2
        self.size = arrlist1.size + arrlist2.size

    def delete(self, index):
        if index > self.max:
            raise Exception('Index Out of Bounds')

        if index == self.size-1: 
            self.list[index] = None
            self.size -= 1

        if index < self.size-1:
            self.list[index] = None
            for i in range(index, self.size-1):
                self.list[i] = self.list[i+1]
            self.list[self.size-1]=None
            self.size -= 1



al = ArrayList()

print(al)
al.push(1)
print(al)
al.push(2)
print(al)
al.push(3)
print(al)
al.push(4)
al.push(5)
print(al)

al2 = ArrayList()
al2.push(3)
al2.push(4)
al2.push(5)
print(al2)

al3 = ArrayList()
al3.merge(al,al2)
print(al3)
al3.delete(10)
al3.delete(5)
al3.delete(0)
print(al3)