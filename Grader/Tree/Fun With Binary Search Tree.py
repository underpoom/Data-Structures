class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            curr = self.root
            while True:
                if data < curr.data:
                    if curr.left is None:
                        curr.left = Node(data)
                        break
                    curr = curr.left
                else:
                    if curr.right is None:
                        curr.right = Node(data)
                        break
                    curr = curr.right
        return self.root
    def printTree(self, node, level = 0) :
        
        if node != None:
            
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    def Preorder(self, node,l) :
        if node != None:
            l.append(node.data)
            self.Preorder(node.left,l)
            self.Preorder(node.right, l)
        return l
    def Inorder(self, node,l) :
        if node != None:
            self.Inorder(node.left,l)
            l.append(node.data)
            self.Inorder(node.right, l)
        return l
    def Postorder(self, node,l) :
        if node != None:
            self.Postorder(node.left,l)
            self.Postorder(node.right, l)
            l.append(node.data)
        return l
    def Maxlevel(self,node,level,l):
        if node != None:
            self.Maxlevel(node.right, level + 1,l)
            self.Maxlevel(node.left, level + 1,l)
            l.append(level)
        return l
    def Withlevel(self,node,level,cl,l):
        if node != None:
            self.Withlevel(node.left, level + 1,cl,l)
            self.Withlevel(node.right, level + 1,cl,l)
            
            
            if level == cl:
                l.append(node.data)
            
        return l


    def Breadth(self,root):
        h = max(self.Maxlevel(root,1,[]))
        l = []
        ll = []
        for i in range(1,h+1):
            l = self.Withlevel(root,1,i,[])
            ll+=l
        
        return ll
    
        

T = BST()
l = [[]*3]
inp = [int(e) for e in input('Enter Input : ').split()]

for i in inp:
    root = T.insert(i)

print('Preorder :',*T.Preorder(root,[]))
print('Inorder :',*T.Inorder(root,[]))
print('Postorder :',*T.Postorder(root,[]))
print('Breadth :',*T.Breadth(root))