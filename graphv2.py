
#directional graph
class Node(object):


    def __init__ (self, value):
        self.value = value
        self.children = []
        self.marked = False


    def addchild(self, node):
        for child in self.children:
            if child.value == node.value:
                print('Child already in Node Adjacency List')
                return 
        self.children += [node]


    def mark(self):
        self.marked = True

    def unmark(self):
        self.marked = False

    def is_marked(self):
        return self.marked

class Graph(object):


    def __init__(self):
        self.graph = []
        self._dfs_found_flag = False


    def __str__(self):
        string  = ''
        for node in self.graph:
            string += str(node.value)+': '
            for nodes in node.children:
                string += str(nodes.value)+' '
            string += '\n'
        return string

    def add(self, value, children: list):
            
            #check if already a node with the value
            flag = False
            for node in self.graph:
                if value == node.value: 
                    print(f'{value} already in graph')
                    new_node = node
                    flag = True
                    break

            # if node not present create a new node
            if flag == False:
                new_node = Node(value)
                self.graph.append(new_node)

            # check if nodes for desired children are already present
            for child in children: 
                present = False
                for node in self.graph:
                    if child == node.value:
                        new_node.addchild(node)
                        present = True
                        break

                # if children not present, create nodes for them
                if present == False: 
                    child_node = Node(child)
                    self.graph.append(child_node)
                    new_node.addchild(child_node)

    def clearMarks(self):
        for node in self.graph:
            node.unmark()

    def getNode(self, value):
        for node in self.graph:
            if node.value == value:
                return node
        return None

    def visit(self, node):
        if g._dfs_found_flag == False:
            print(node.value)
        return node.value
        
    def BFS(self, root, value):
        g.clearMarks()
        print('BFS:')
        queue = []
        root.mark()
        queue.append(root)

        while(queue):
            node = queue.pop(0)
            if g.visit(node) == value:
                print('{} found.'.format(value))
                break
            for child in node.children:
                if child.is_marked() == False:
                    child.mark()
                    queue.append(child)
        print('BFS Complete.\n')
        g.clearMarks()


    def DFS(self, root, value):
        g.clearMarks()
        g._dfs_found_flag = False
        print('DFS:')
        g._DFS(root, value)
        g._dfs_found_flag = False
        print('{} found.\nDFS complete\n'.format(value))

    def _DFS(self,root,value):
        if root == None: return
        if g.visit(root) == value: 
            g._dfs_found_flag = True
            return True
        root.mark()
        for child in root.children:
            if child.is_marked() == False:
                if g._DFS(child, value): return


g = Graph()
"""
g.add(10, [9,2])
g.add(9,[1,4])
g.add(8,[])
g.add(7,[9,5,4,3])
g.add(6,[7])
g.add(5,[])
g.add(4,[8,6,2])
g.add(3,[2,1])
g.add(2,[1])
g.add(1,[])
"""

g.add('a', ['b','d','e','g','i'])
g.add('b', ['c','d','a'])
g.add('c', ['b',10])
g.add('d', ['a','e','b','h'])
g.add('e',['a','d','f'])
g.add('f',['g','e','d','j'])
g.add('g',['a','f'])
g.add('h',['d','j'])
g.add('i',['a'])
g.add('j',['h','f','k'])
g.add('k',['j','l'])
g.add('l',['k','m'])
g.add('m',['l',7])
g.add(1,[2,4,5,6,8])
g.add(2,[1,3,7])
g.add(3,[2])
g.add(4,[1,12])
g.add(5,[1,8,11])
g.add(6,[1,7,8])
g.add(7,[2,3,6,'m'])
g.add(8, [1,5,6,9])
g.add(9,[8,10])
g.add(10,['c',9])
g.add(11,[5])
g.add(12,[4])

print(g)

g.BFS(g.getNode('a'), 1)

g.DFS(g.getNode('a'), 1)

g.BFS(g.getNode(10), None)

g.DFS(g.getNode(10),None)


