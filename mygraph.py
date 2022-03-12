

class Graph(object):

    def __init__(self):

        self.graph = []


    def print(self):
        print('Printing Graph:')
        for node in self.graph:
            print(node)


    def addnode(self, value = None):

        if value != None: 
            for node in self.graph: 
                if value == node[0]: 
                    print('Node '+ value +' already entered in graph')
                    return
            self.graph.append([value, []])

        else: 
            print('No value added for new Graph Node')

    # adds edges between nodes (vertices)
    # Can be used to update edges
    # node1 first vertices
    # node2 second vertices
    # weight - weight of the edge joining the first vertices
    # dir - if True only applies the vertices from node1 to node2 (not node2 to node1)
    def addedge(self, node1 = None, node2=None, weight = 1, dir = False):

        if node1 == None or node2 == None: 
            print('Node values not properly input for adding edge')
            return

        n1_flag = n2_flag = False
        for nodes in self.graph: 
            if node1 ==  nodes[0]: n1_flag = True
            if node2 ==  nodes[0]:  n2_flag = True
            if n1_flag == n2_flag == True: break

        if n1_flag == False or n2_flag == False:
            print ('One or both nodes is not present in Graph')
            return

        addededge12 = False
        for nodes in self.graph: 
            if node1 == nodes[0]: 
                # if edge is already present
                for adjnodes in nodes[1]:
                    if node2 == adjnodes[0]:
                        adjnodes[1] = weight
                        adjnodes[2] = dir
                        print('Edge ',node1,'-', node2, ' is already present, updated weight and dir')
                        addededge12 = True
                        break
                
                # else add the edge
                if addededge12 == False:
                    nodes[1].append([node2, weight, dir])
                    print('Added Edge: ', node1, node2, weight, dir)
                    addededge12 == True

        # handles non-directional edges
        if dir == False: 
            addededge21 = False
            for nodes in self.graph: 
                if node2 == nodes[0]: 
                    # if edge is already present
                    for adjnodes in nodes[1]:
                        if node1 == adjnodes[0]:
                            adjnodes[1] = weight
                            adjnodes[2] = dir
                            print('Edge ', node2,'-', node1,' is already present, updated weight and dir')
                            addededge21 = True
                            break

                    # else add the edge
                    if addededge21 == False:
                        nodes[1].append([node1, weight, dir])
                        print('Added Edge: ', node2, node1, weight, dir)


    # deletes edge. If dir = True, deletes the edge only in the direction
    # that is specified by node1 -> node2. 
    def deledge(self, node1 = None, node2 = None, dir = False):
        if node1 == None or node2 == None: 
            print('Node values not properly input for deleting edge')
            return

        n1_flag = n2_flag = False
        for nodes in self.graph: 
            if node1 ==  nodes[0]: n1_flag = True
            if node2 ==  nodes[0]:  n2_flag = True
            if n1_flag == n2_flag == True: break

        if n1_flag == False or n2_flag == False:
            print ('One or both nodes is not present in Graph')
            return

        for nodes in self.graph: 
            if node1 == nodes[0]:
                for adjnodes in nodes[1]: 
                    if node2 == adjnodes[0]: 
                        nodes[1].remove(adjnodes)

            elif dir == False:
                if node2 == nodes[0]:
                    for adjnodes in nodes[1]:
                        if node1 == adjnodes[0]:
                            nodes[1].remove(adjnodes)


    # Deletes node (vertex) and any edges connecting to it from other nodes. 
    def delnode(self, node = None):
        if node == None: 
            print('Node value not input for deletion.')
            return

        for nodes in self.graph: 
            for adjnodes in nodes[1]: 
                if node == adjnodes[0]:
                    nodes[1].remove(adjnodes)
            if node == nodes[0]: 
                self.graph.remove(nodes)
