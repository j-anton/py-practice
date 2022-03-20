
from itertools import permutations


class Hashnode(object):
	
	def __init__(self, key=None, value=None):
		self.key = key
		self.value = value
		self.next = None


	def dump(self):
		node = self
		while (node != None):
			print(node.key,node.value, node.next)
			node = node.next
		

class Hashtable(object):
	

	def dump(self):
		for i, elem in enumerate(self.hashtable):
				if elem != None:
					print ('Hash:{i}'.format(i=i))
					elem.dump()
			
	
	def __hash(self, key, tablesize):

		if (isinstance(key, str)):
			
			value = 0
			for i, char in enumerate(key):
				value += ord(char)*10**i
			return value % tablesize

		if (isinstance(key, (float,int))):
			
			return key % tablesize
		
		if (isinstance(key, (dict, list, tuple))):
		
			print('Unsupported key type.')
			return None

		if (key == True):
			
			return key % tablesize
		
		if (key == None): 
			
			return key%tablesize

		if (key == False):
			
				return key % tablesize

		else: return None


	def __init__(self, key=None, value=None, size = None):
		
		if (key == None and value != None or key != None and value == None): 
			
			print('Expected initial key,value pair')
			return;

		if isinstance(size, int):
			self.tblsize = size
		else:
			self.tblsize = 11

		self.nodecount = 0
		self.loadfactor = 0
		self.hashtable = [None]*self.tblsize

		if (key!=None and value != None):
			
			
			self.nodecount += 1
			self.__sizecheck()
			new_node = Hashnode(key, value)
			hashed = self.__hash(key, self.tblsize)
			self.hashtable[hashed] = new_node
			#print('DEBUG: __inti__, adding Node: key:{key}, value:{value}.'.format(key=key,value=value))


	def insert(self, key, value):
	
		if (key == None):
			print('Key must be entered for key,value')

		hashed = self.__hash(key, self.tblsize)

		if self.hashtable[hashed] == None:
			self.nodecount += 1
			new_node = Hashnode(key, value)
			self.hashtable[hashed]=new_node
			#print('DEBUG: Empty index, adding Node: key:{key}, value:{value}.'.format(key=key,value=value))
			self.__sizecheck()
			return

		else: 
			node = self.hashtable[hashed]
			while(node != None):
				# overwrite the preexisting value for the given key
				if node.key == key: 
					node.value = value
					return

				# At the end of the list if key is not found,
				# add a new node with key:value
				if (node.next == None): 
					self.nodecount += 1
					new_node = Hashnode(key, value)
					node.next = new_node
					self.__sizecheck()
					return

				node = node.next

		print ('DEBUG: main->insert: SHOULD NEVER GET HERE')
		return None
	

	# find item in hash table.
	# if item in hash table return item 
	# if item not in hash table return None
	def search(self, key):

		hashed = self.__hash(key,self.tblsize)

		if self.hashtable[hashed] == None:
			print('No value for {key} in hashtable'.format(key=key))
			return None

		else: 
			node_ptr = self.hashtable[hashed]

			while (node_ptr != None):
				if node_ptr.key == key:
					return node_ptr.value
				node_ptr = node_ptr.next
		
			print('No value for {key} in hashtable'.format(key=key))
			return None


	def __resize(self):
		# double size of hashtable rounded up to nearest prime. 
		# recalculate all the hashes
		print('RESIZING ARRAY: ')

		new_hashtable = [None]* self.tblsize*2

		for i, old_head_node in enumerate(self.hashtable):
			
			old_node_ptr = old_head_node
			
			while old_node_ptr != None: 
		
				hashed = self.__hash(old_node_ptr.key, self.tblsize*2)

				if new_hashtable[hashed] == None:
					new_node = Hashnode(old_node_ptr.key, old_node_ptr.value)
					new_hashtable[hashed]=new_node
					#print('added to new_hashtable')
					
				else:
					node_ptr = new_hashtable[hashed]
					while(node_ptr != None):
						# At the end of the list if key is not found,
						# add a new node with key:value
						if (node_ptr.next == None): 
							new_node = Hashnode(old_node_ptr.key, old_node_ptr.value)
							node_ptr.next = new_node
							break;

					node_ptr = node_ptr.next

				old_node_ptr = old_node_ptr.next
	
		self.hashtable = new_hashtable
		self.tblsize *= 2

			
	def __sizecheck(self):
		
		self.loadfactor = self.nodecount/self.tblsize
		if (self.loadfactor > 0.7):
			self.__resize()
			print('__sizecheck(): Resize ordered: {count}, {size}'.format(count=self.nodecount, size = self.tblsize))



# Testing
table = Hashtable()

combos = permutations(['a','b','c','d','e','f','g','h','i'], 2)
for i, elem in enumerate(combos):
	table.insert(i, elem)

table.dump()

print(table.search(20))
print(table.search(50))
print(table.search(100))
print(table.search(200))









	
