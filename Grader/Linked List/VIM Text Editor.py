import math
class LinkedList :
    class Node :
        def __init__(self,data,prev = None,next = None) :
            self.data=data
            if prev is None :
                self.prev = None
            else :
                self.prev = prev

            if next is None :
                self.next = None
            else :
                self.next = next
    def __init__(self):                
            self.head = None
            self.size = 0
    def __str__(self):
        s = ''
        p = self.head
        for i in range(len(self)) :
            s += str(p.data) + ' '
            p = p.next
        return s
    def __len__(self) :
        return self.size
    def isEmpty(self) :
        return self.size == 0
    def _print(self):
        if self.size == 0:
            return 'Empty'
        current = self.head
        s = ''
        while current:
            s+=str(current.data)+' '
            current = current.next
        return s
    def index(self,data) :
        q = self.head
        for i in range(len(self)) :
            if q.data == data :
                return i
            q = q.next
        return -1
    def isIn(self,data) :
        return self.index(data) >= 0
    def nodeAt(self,i) :
        p = self.head
        for j in range(i) :
            p = p.next
        return p
    def size(self):
        return self.size
   
    def append(self,data) :
        if self.head == None :
            self.head = self.Node(data)
            self.size += 1
        else :
            q = self.nodeAt(len(self)-1)
            x = self.Node(data,q,None)
            q.next = x
            self.size += 1
    
    def removeNode(self,q) :
        p = q.prev
        x = q.next
        p.next = x
        x.prev = p
        self.size -= 1

    def delete(self,i) :
        if i<0 or i>=self.size:
            return print('Out of Range' )
        if i == 0 :
           
            self.head = self.head.next
            self.prev = None
            self.size -= 1
            return
           
        elif i == len(self) - 1 :
            x = self.nodeAt(i)
            p = x.prev
            p.next = None
            self.size -= 1
            return
        else:
            self.removeNode(self.nodeAt(i))
            return

    def insert(self,id,data) :
        if id == self.size:
            return self.append(data)
        q = self.nodeAt(id)
        if self.size == 0:
            if self.head == None :
                self.head = self.Node(data)
                self.size += 1
                return
            else :
                q = self.nodeAt(len(self)-1)
                x = self.Node(data,q,None)
                q.next = x
                self.size += 1
                return
        if q.prev == None :
            new_node = self.Node(data)
            new_node.next = self.head 
            if self.head is not None:
                self.head.prev = new_node      
            self.head = new_node
            self.size += 1  
            return 
        else:
            p = q.prev
            x = self.Node(data,p,q)
            p.next = q.prev = x
            self.size += 1  
            return q

    def remove_left(self,id) :
        if id>0:
            return self.delete(id-1)

    def remove_right(self,id):
        if id<self.size:
            return self.delete(id)

ll = LinkedList()
id = 0
s = input('Enter Input : ')

for i in s.split(','):
    i = i.split()
    if i[0]=='I':
        ll.insert(id,i[1])
        id+=1
    elif i[0]=='L':
        if id>0:
            id-=1
    elif i[0]=='R':
        if id<ll.size:
            id+=1
    elif i[0]=='B':
        ll.remove_left(id)  
        if id>0:
            id-=1
    elif i[0]=='D':
        ll.remove_right(id)
        
if id!=0:
    ll.insert(id,'|')
else:
    print('|',end=' ')
print(ll._print())