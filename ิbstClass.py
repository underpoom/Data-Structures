class Node:
    def __init__(self,key = None):
        self.rChild = None
        self.lChild = None
        self.parent = None
        self.data = key 

class Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self,someNumber):
        self.size = self.size+1
        if self.root is None:
            self.root = Node(someNumber)
        else:
            self.insertWithNode(self.root, someNumber)    

    def insertWithNode(self,node,someNumber):
        if node.lChild is None and node.rChild is None:
            if someNumber > node.data:
                newNode = Node(someNumber)
                node.rChild = newNode
                newNode.parent = node
            else:
                newNode = Node(someNumber)
                node.lChild = newNode
                newNode.parent = node
        else: 
            if someNumber > node.data:
                if node.rChild is not None:
                    self.insertWithNode(node.rChild, someNumber)
                else: 
                    newNode = Node(someNumber)
                    node.rChild = newNode
                    newNode.parent = node 
            else:
                if node.lChild is not None:
                    self.insertWithNode(node.lChild, someNumber)
                else:
                    newNode = Node(someNumber)
                    node.lChild = newNode
                    newNode.parent = node                    
    def _pre(self):
        print( ' '.join([str(e) for e in self.preorder(self.root,[])])  )
    def _in(self):
        print( ' '.join([str(e) for e in self.inorder(self.root,[])])  )
    def _post(self):
        print( ' '.join([str(e) for e in self.postorder(self.root,[])])  )
    def _printtree(self):
        self.printtree(self.root)
        
    def preorder(self,someNode,l):
        if someNode:
            l.append(someNode.data)
            self.preorder(someNode.lChild,l)
            self.preorder(someNode.rChild,l)
        return l

    def inorder(self,someNode):
        if someNode:
            self.inorder(someNode.lChild)
            print( someNode.data)
            self.inorder(someNode.rChild)
        
    def postorder(self,someNode):
        if someNode:
            self.postorder(someNode.lChild)
            self.postorder(someNode.rChild)
            print( someNode.data)

    def printtree(self, node, level = 0) :
        if node != None:
            self.printtree(node.rChild, level + 1)
            print('     ' * level, node.data)
            self.printtree(node.lChild, level + 1)

def deleteNode(root, data):
 
    if root is None:
        return root

    if data < root.data:
        root.lChild = deleteNode(root.lChild, data)
    elif(data > root.data):
        root.rChile = deleteNode(root.rChild, data)
    else:

        if root.lChild is None:
            temp = root.rChild
            root = None
            return temp
 
        elif root.rChild is None:
            temp = root.lChild
            root = None
            return temp

        temp = minValueNode(root.rChild)

        root.data = temp.data
 
        root.rChild = deleteNode(root.rChild, temp.data)
 
    return root

def minValueNode(node):
    current = node
    while(current.left is not None):
        current = current.lChild
 
    return current
t = Tree()
s = '1'
l = [int(e) for e in s.split()]

for i in l:
    t.insert(i)


t._printtree()
print('--------------------------------------')
t.root = deleteNode(t.root,1)
t._printtree()
print('--------------------------------------')
t.insert(1)
t._printtree()

    
