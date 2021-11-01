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
      

    def lprintTree(self, node,l) :
        
        if node != None:
            self.lprintTree(node.left,l)
            l.append(node.data)
            self.lprintTree(node.right, l)
            
        return l
     
        

T = BST()
l = []
inp = input('Enter Input : ')
inp = inp.split('|')
k = int(inp[1])
inp[0] = [int(e) for e in inp[0].split()]
for i in inp[0]:
    root = T.insert(i)
T.printTree(root)
l = T.lprintTree(root,[])
print('--------------------------------------------------')



if min([int(e) for e in l]) < k:
    print( 'Below',k,':', ' '.join( [str(e) for e in l if e < k   ] ) )
    
else:
    print( 'Below '+str(k),':', 'Not have' ) 