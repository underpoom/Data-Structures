class Node:
    

    def __init__(self,key):
        self.rChild = None
        self.lChild = None
        self.data = key 

class Tree:
    def __init__(self):
        self.root = None
        self.size = 0                
    def _pre(self):
        return ( ''.join([str(e) for e in self.preorder(self.root,[])])  )
    def _post(self):
        st = Stack()
        for i in l:
            if i.isalpha():
                st.push(i)
            else:
                a = st.pop()
                b = st.pop()
                st.push('('+ b + i + a +')')
        return ( ''.join([str(e) for e in st.items]))

    def _printtree(self):
        self.printtree(self.root)

    def preorder(self,someNode,l):
        if someNode:
            l.append(someNode.data)
            self.preorder(someNode.lChild,l)
            self.preorder(someNode.rChild,l)
        return l
        
    def postorder(self,someNode,l):
        if someNode:
            self.postorder(someNode.lChild,l)
            self.postorder(someNode.rChild,l)
            l.append(someNode.data)
        return l

    def printtree(self, node, level = 0) :
        if node != None:
            self.printtree(node.rChild, level + 1)
            print('     ' * level, node.data)
            self.printtree(node.lChild, level + 1)

class Stack:
    def __init__(self):
        self.items = []
    def push(self, i):
        return self.items.append(i)
    def pop(self):
        return self.items.pop()

st = Stack()
T = Tree()

l = [e for e in input('Enter Postfix : ')]

for i in l:
    if i.isalpha():
        st.push(Node(i))
    else:
        curr = Node(i)
        curr.rChild = st.pop()
        curr.lChild = st.pop()
        st.push(curr)
T.root = st.pop()

print('Tree :')
T._printtree()
print('--------------------------------------------------')
print('Infix :',T._post())
print('Prefix :',T._pre())