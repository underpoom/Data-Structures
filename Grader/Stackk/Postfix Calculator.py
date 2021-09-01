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
   
    

s = input(' ***Postfix expression calcuation***\nEnter Postfix expression : ').split()
d=Stack()
for i in s:
    if i not in '+-*/':
        d.push(int(i))
    if i=='+':
        y = d.pop()
        x = d.pop()
        d.push(x+y)
    elif i=='-':
        y = d.pop()
        x = d.pop()
        d.push(x-y)
    elif i=='*':
        y = d.pop()
        x = d.pop()
        d.push(x*y)
    elif i=='/':
        y = d.pop()
        x = d.pop()
        d.push(x/y)
    
x = d.items[0]
print("Answer :  {:0.2f}".format(x))