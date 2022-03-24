
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
            if g.visit(node) == value: break
            for child in node.children:
                if child.is_marked() == False:
                    child.mark()
                    queue.append(child)
        print('{} found, BFS complete\n'.format(value))
        g.clearMarks()


    def DFS(self, root, value):
        g.clearMarks()
        print('DFS:')
        g._DFS(root, value)
        print('{} found, DFS complete\n'.format(value))

    def _DFS(self,root,value):
        found = False
        if root == None: return
        if g.visit(root) == value: return True
        root.mark()
        for child in root.children:
            if child.is_marked() == False:
                if g._DFS(child, value): return




g = Graph()
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

print(g)

g.BFS(g.getNode(10), 7)

g.DFS(g.getNode(10), 7)

g.BFS(g.getNode(10), None)

g.DFS(g.getNode(10),None)


