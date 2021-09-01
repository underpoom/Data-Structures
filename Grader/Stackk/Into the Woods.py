import re
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
s = s.replace('B','0')
d = Stack()
v = re.findall('\d+',s)
for i in v :
    if(i!='0'):
        if(d.size()==0 or int(i)<d.top()):
            d.push(int(i))
        else:
            while (d.size()!=0 and int(i)>=d.top()):
                d.pop()
            d.push(int(i))

        
    if i=='0':
        print(d.size())