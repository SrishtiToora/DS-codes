import _collections
class node:
    def __init__(self,key,left=None,right=None,parent=None):
        self.key=key
        self.left_child = left
        self.right_child = right
        self.parent = parent


class binary_search_tree(node):
    def __init__(self):
        self.root=None
        self.size=0
        self.height=0

    def length(self):
        return self.size

    def insert(self,key):
        if self.root==None:
            self.root=node(key)
            self.height +=1
        else:
            self._insert(key,self.root)
        self.size += 1

    def _insert(self,key,currentnode):
        if key<currentnode.key:
            if currentnode.left_child==None:
                currentnode.left_child=node(key,parent=currentnode)
            else:
                self._insert(key,currentnode.left_child)
        elif key > currentnode.key:
            if currentnode.right_child==None:
                currentnode.right_child=node(key,parent=currentnode)
            else:
                self._insert(key,currentnode.right_child)
        else:
            print ("key already in tree")

    def findMin(self,key):
        current=self.get(key)
        while current.left_child!=None:
            current = current.left_child
        return current.key


    def findSuccessor(self,key):
        currentnode=self.get(key)
        succ = None
        suc=None
        if currentnode.right_child!=None:
            succ = self.findMin(currentnode.right_child.key)
        else:
            if currentnode.parent!=None:

                if currentnode.parent.left_child==currentnode:
                    suc = currentnode.parent.key
                else:
                    currentnode.parent.right_child = None
                    suc = self.findSuccessor(currentnode.parent.key)
                    currentnode.parent.right_child =currentnode
            succ=suc
        return succ

    def get(self, key):
        if self.root!=None:
            res = self._get(key, self.root)
            if res.key!=None:
                return res
            else:
                return None
        else:
            return None

    def _get(self, key, currentnode):
        if currentnode==None:
            return None
        elif currentnode.key == key:
            return currentnode
        elif key < currentnode.key:
            return self._get(key, currentnode.left_child)
        else:
            return self._get(key, currentnode.right_child)

    def contains(self, key):
        if self.get(key)!=None:
            return True
        elif self.get(key) == None:
            return False

    def remove(self,currentnode):
        if currentnode.right_child==None and currentnode.left_child==None:
            if currentnode.parent.left_child==currentnode:
                currentnode.parent.left_child=None
            elif currentnode.parent.right_child==currentnode:
                currentnode.parent.right_child=None
        elif currentnode.right_child==None or currentnode.left_child==None:
            if currentnode.left_child!=None:
                if currentnode.parent.left_child==currentnode:
                    currentnode.left_child.parent=currentnode.parent
                    currentnode.parent.left_child=currentnode.left_child
                if currentnode.parent.right_child==currentnode:
                    currentnode.left_child.parent=currentnode.parent
                    currentnode.parent.right_child=currentnode.left_child
            elif currentnode.right_child!=None:
                if currentnode.parent.left_child==currentnode:
                    currentnode.parent.left_child=currentnode.right_child
                    currentnode.right_child.parent=currentnode.parent
                if currentnode.parent.right_child==currentnode:
                    currentnode.parent.right_child=currentnode.right_child
                    currentnode.right_child.parent=currentnode.parent
        elif currentnode.right_child!=None and currentnode.left_child!=None:
            succKey=self.findSuccessor(currentnode.key)
            succ=self.get(succKey)
            self.removingSuccessor(succ)
            currentnode.key=succ.key


    def removingSuccessor(self,rnode):
        if rnode.right_child == None and rnode.left_child == None:
            if rnode.parent.left_child==rnode:
                rnode.parent.left_child=None
            else:
                rnode.parent.right_child=None
        elif rnode.right_child == None or rnode.left_child == None:
            if rnode.right_child!=None:
                rnode.right_child.parent=rnode.parent
                rnode.parent.left_child=rnode.right_child

    def deletingaAKey(self,delkey):
        delnode=self.get(delkey)
        self.remove(delnode)


    def getHeight(self,root): #node perimeter
        if root!=None:
            if root.left_child!=None and root.right_child!= None:
                return 1+max(self.getHeight(root.left_child),self.getHeight(root.right_child))
            elif root.left_child!=None:
                return 1 + self.getHeight(root.left_child)
            elif root.right_child!=None:
                return 1+ self.getHeight(root.right_child)
            else:
                return 1
        else:
            return 0









tree = binary_search_tree()
tree.insert(5)
tree.insert(10)
tree.insert(6)
tree.insert(3)
tree.insert(4)
tree.insert(20)
tree.insert(7)
tree.insert(2)
tree.insert(1)
print(tree.root.key)                        #1
print(tree.root.left_child.right_child.key) #2
print(tree.root.right_child.left_child.key) #3
vgf=tree.findMin(4)
print(vgf)                                  #4
vgf2=tree.findMin(6)
print(vgf2)                                 #5
vgf3=tree.findSuccessor(4)
print(vgf3)                                 #6
#tree.deletingaAKey(11)
print(tree.root.right_child.key)            #7
print(tree.getHeight(tree.root))  #8
print(tree.contains(100))


















