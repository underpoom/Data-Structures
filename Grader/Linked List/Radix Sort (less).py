import math
class LinkedList :
    class Node :
        def __init__(self,data) :
            self.data = data
            self.next = None

    def __init__(self):                
            self.head = None
            self.size = 0
   
    def _print(self):
        if self.size == 0:
            return ''
        current = self.head
        s = ''
        while current:
            s+=str(current.data)+' '
            current = current.next
        return s
    
    def push(self,data):
        current = self.head
        new_node = self.Node(data)
        if current is None:
            self.head = new_node
            self.size += 1  
            return 
        if current.data < data:
            new_node.next = current
            self.head = new_node
            self.size += 1  
            return
        while(current.next != None):
            if current.data > data and current.next.data < data:
                break
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self.size += 1  
        return

def dec(x,n):
    if x==0:
        return 0
    if x<0:
        x = abs(x)
    digit = int(math.log10(x))+1
    if digit>=n:
        return int(str(x)[digit-n:digit-n+1])
    return 0

s = input('Enter Input : ')
s = [int(e) for e in s.split()]
cps = s
digit = 0
l = []
n = [LinkedList() for i in range(10)]
n_0 = 0
while(n[0].size<len(cps)):
    digit+=1
    for i in s:
        n[dec(i,digit)].push(i) 
    for i in range(1,10) :
        if n[i].size != 0:
            for e in n[i]._print().split():
                l.append(int(e))
    s = l.copy()
    l.clear()
 
    print('------------------------------------------------------------\nRound :',digit)
    print(str(0),':',n[0]._print())
    for i in range(1,10):
        print(str(i),':',n[i]._print())
        n[i] = LinkedList()
print('------------------------------------------------------------')
print(str(digit-1) + ' Time(s)')
print('Before Radix Sort : '+' -> '.join([str(e) for e in cps]))
print('After  Radix Sort : '+' -> '.join([str(e) for e in n[0]._print().split()]))