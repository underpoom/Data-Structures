class Stack:
    def __init__(self):
        self.items = []
    def push(self, i):
        return self.items.append(i)
    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        return (len(self.items)==0)
    def size(self):
        return len(self.items)
    def top(self):
        if self.size()!=0:
            return self.items[-1]
    def __str__(self):
        return str(self.items)


s = input('Enter Input : ')
d=Stack()
s=s.split(',')
for i in s:
    if len(i)!=1:
        if(i[0]=='A'):
            i=i.split()
            d.push(int(i[1]))
            print('Add =',d.top() ,'and Size =', str(d.size()))
    elif i[0]=='P':
        if(d.size()==0):
            print('-1')
        else:
            temp = d.top()
            d.pop()
            print('Pop =',temp ,'and Index =', str(d.size()))
         
if(d.size()==0):
    print('Value in Stack = Empty ')
else:
    print('Value in Stack =' , *[str(e) for e in d.items])