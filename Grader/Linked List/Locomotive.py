class Node:
    def __init__(self,data):
        self.data=data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
    def __str__(self):
        current = self.head
        s = ''
        while(current!=None):
            s+=str(current.data)
            current = current.next
        return ' <- '.join(s)
    
    def push_tail(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return 
        current = self.head
        while(current.next):
            current = current.next
        current.next = new_node
        new_node.next=None

ll = Linkedlist()
ll1 = Linkedlist()
ll2 = Linkedlist()

print(' *** Locomotive ***')
s = [int(e) for e in input('Enter Input : ').split()]

for i in s:
    ll.push_tail(i)
v = 0
for i in s:
    if i==0:
        v=1
    if v==1:
        ll1.push_tail(i)
for i in s:
    if i == 0:
        break
    ll1.push_tail(i)
    
print('Before :',ll)
print('After :',ll1)