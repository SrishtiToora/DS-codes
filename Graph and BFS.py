class queue():
    def __init__(self):
        self.items=[]
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

class Vertex:
    def __init__(self, vertexKey):
        self.id = vertexKey
        self.connectedTo = []
        self.colour='white'
        self.distance=0
        self.pre=None

    def addNbr(self, nbr):
        self.connectedTo.append(nbr)

    def getConnections(self):
        return self.connectedTo

    def getId(self):
        return self.id


class Graph:
    def __init__(self):
        self.numVertices = 0
        self.vertList = {}

    def addVertex(self, Key):
        self.numVertices += 1
        newVertex = Vertex(Key)
        self.vertList[Key] = newVertex

    def getVertex(self, key):
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None

    def __contains__(self, key):
        return key in self.vertList

    def addEdge(self, v1, v2):
        if v1 not in self.vertList:
            self.addVertex(v1)
        if v2 not in self.vertList:
            self.addVertex(v2)
        self.vertList[v1].addNbr(self.vertList[v2])
        self.vertList[v2].addNbr(self.vertList[v1])

    def getVertices(self):
        return self.vertList.keys()  # if .vertices then that whole vertex

    def bfs(self, start):
        VertQueue = queue()
        VertQueue.enqueue(self.getVertex(start))   #can insert only one type of data in queue
        listOfVertices = []
        while VertQueue.size() > 0:
            currentVertex = VertQueue.dequeue()

            listOfVertices.append(currentVertex.getId())   # currentVertex > currentVertex.getId()
            # print("==========listOfVertices", listOfVertices)
            #print("=========currentVertkey", currentVertex)
            for nbr in currentVertex.getConnections():
                #print("=========currentVertex.colour", currentVertex.colour)
                if nbr.colour == 'white':
                    nbr.colour = 'grey'
                    # print("==========================================")
                    nbr.distance = currentVertex.distance + 1
                    nbr.pre = currentVertex
                    VertQueue.enqueue(nbr)
            currentVertex.colour = 'black'
            # try:

            #     # print("=========currentVertex.colour", currentVertex.colour)
            # except AttributeError:
            #     print("========////////////////////////////---------", currentVertex)

        return listOfVertices

g1=Graph()
g1.addVertex(1)
g1.addVertex(2)
g1.addVertex(4)
g1.addVertex(3)
g1.addEdge(1,2)
g1.addEdge(2,3)
g1.addEdge(3,4)
print(g1.bfs(2))


















