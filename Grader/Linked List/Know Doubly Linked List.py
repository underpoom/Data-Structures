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
    
    def index(self,data) :
        q = self.head
        for i in range(len(self)) :
            if q.data == data :
                return i
            q = q.next
        return -1
    def search(self,data):
        if self.isIn(data) == 0:
            print('Not Found ' + data + ' in '+ self._print())
        else:
            print('Found ' + data + ' in '+ self._print())
    def search_index(self,data):
        if self.index(data) == -1:
            print('Index (' + data + ') = -1 : ' + self._print())
        else:
            print('Index (' + data + ') = '+ str(self.index(data)) + ' : ' + self._print())
    
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
            return print('Out of Range | ' + ll._print())
        if i == 0 :
            print('Success | '+self.nodeAt(i).data +' -> ',end='')
            self.head = self.head.next
            self.prev = None
            self.size -= 1
            print(self._print())
        elif i == len(self) - 1 :
            x = self.nodeAt(i)
            p = x.prev
            p.next = None
            self.size -= 1
        else:
            self.removeNode(self.nodeAt(i))

    def insert(self,q,data) :
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
#
    def _print(self):
        if self.size == 0:
            return 'Empty'
        current = self.head
        s = ''
        while current:
            s+=str(current.data)+' '
            current = current.next
        return s

    def rev(self):
        if self.size==0:
            return 'Empty'
        s =''
        current = self.head
        while current.next:
            current = current.next
        last = current
        while last:
            s+=last.data+' '
            last = last.prev
        return s

def correct_id(a,b):
    if abs(a)<=b:
        return b-abs(a)
    if a>b:
        return b
    if a<0:
        return 0
    return a

ll = LinkedList()

s = input('Enter Input : ')

for i in s.split(','):
    i = i.split()
    if i[0]=='AP':
        ll.append(i[1])
    elif i[0]=='AH':
        ll.insert(ll.head,i[1])
    elif i[0]=='SE':
        ll.search(i[1])
    elif i[0]=='SI':
        print('Linked List size = '+str(ll.size) + ' : ' + ll._print())
    elif i[0]=='ID':
        ll.search_index(i[1])
    elif i[0]=='PO':
        ll.delete(int(i[1]))
    elif i[0]=='IS':
        if correct_id(int(i[1]),ll.size) == ll.size:
            ll.append(i[2])
        else:
            ll.insert(ll.nodeAt(correct_id(int(i[1]),ll.size)), i[2] )
    
print('Linked List :',ll._print())
print('Linked List Reverse :',ll.rev())