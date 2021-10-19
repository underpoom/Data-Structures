class Stack:
    def __init__(self):
        self.items = []
    def push(self, i):
        return self.items.append(i)
    def pop(self):
        return self.items.pop()

def cal(i,y,x):
    return {
        '+' : x+y,
        '-' : x-y,
        '*' : x*y,
        '/' : x/y
    }[i]
    
s = input(' ***Postfix expression calcuation***\nEnter Postfix expression : ').split()
d=Stack()
for i in s:  
        d.push(int(i)) if i not in '+-*/' else d.push(cal(i,d.pop(),d.pop()))
    
x = d.items[0]
print("Answer :  {:0.2f}".format(x))
