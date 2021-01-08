class maxBinaryheap:
    def __init__(self):
        self.heapList=[0]
        self.currentSize=0

    def percUp(self,i):
        while i//2>0:
            if self.heapList[i]>self.heapList[i//2]:
                tmp=self.heapList[i//2]
                self.heapList[i//2]=self.heapList[i]
                self.heapList[i]=tmp
            i=i//2

    def insert(self,k):
        self.heapList.append(k)
        self.currentSize=self.currentSize+1
        self.percUp(self.currentSize)

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.maxChild(i)
            if self.heapList[i] < self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def maxChild(self,i):
        if i*2+1>self.currentSize:
            return i*2
        else:
            if self.heapList[i*2+1]>self.heapList[i*2]:
                return i*2+1
            else:
                return i*2

    def delmax(self):
        retval=self.heapList[1]
        self.heapList[1]=self.heapList[self.currentSize]
        self.currentSize=self.currentSize-1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def buildHeap(self,alist):
        i=len(alist)//2
        self.currentSize=len(alist)
        self.heapList=[0]+ alist[:]
        while i>0:
            self.percDown(i)
            i=i-1
    def popu(self,i):
        return self.heapList[i]
    def heapSortlist(self):
        sortedlist=[]
        for i in range(len(self.heapList)):
            sortedlist.append(self.heapList[i])
        return sortedlist


bh = maxBinaryheap()
bh.buildHeap([9,5,6,2,3])

print(bh.delmax())
print(bh.delmax())
print(bh.delmax())
print(bh.delmax())
print(bh.delmax())

bhi=maxBinaryheap()
bhi.buildHeap([27,17,3,16,13,10,1,5,7,12,4,8,9])
print(bhi.popu(-1))
#bhi.percDown(3)


bh4=maxBinaryheap()
bh4.buildHeap([5,3,17,10,84,19,6,22,9])
print(bh4.popu(2))
print(bh4.popu(3))
print(bh4.popu(4))
print(bh4.heapSortlist())
bh4.insert(90)
print(bh4.popu(1))

for i in range(0,6):
    print(i)

