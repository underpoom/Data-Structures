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
s = input('here : ')
op = {'+','-','*','/','(',')','^'}
pr = {'+':1,'-':1,'*':2,'/':2,'^':3}
d = Stack()

op1 =""
for i in s:
    if i not in op:
        op1+=i
    elif i=='(':
        d.push(i)
    elif i==')':
        while d.size()!=0 and d.top()!='(':
            op1+=d.pop()
        d.pop()
    else:
        while d.size()!=0 and d.top()!='(' and pr[i]<=pr[d.top()] :
            op1+=d.pop()
        d.push(i)
while d.size()!=0:
    op1+=d.pop()
print("Postfix : "+op1)


