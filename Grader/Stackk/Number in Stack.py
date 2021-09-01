import re
v = ''
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
    def A(self,d,i):
        print('Add = '+ i)
        d.push(int(i))
    def P(self,d):
        if d.size()==0:
            print('-1')
        else :
            print('Pop =',d.top())
            d.pop()

    def D(self,d,i):
        for j in range(d.size()):
            if( int(i) == d.items[j]):
                if(d.items[j]!=-99999):
                    print('Delete = ' +i)
                d.items[j]=-99999
        if -99999 in d.items:
            d.items.remove(-99999)
        if d.size()==0:
            print('-1')  

    def LD(self,d,i):
        for j in range(d.size()-1,-1,-1):
            if d.items[j]<int(i):
                if(d.items[j]!=-99999):
                    v = ' Because ' + str(d.items[j]) +  ' is less than ' + i
                    print('Delete = '+str(d.items[j]) +v)
                d.items[j]=-99999
        if -99999 in d.items:
            d.items.remove(-99999)
        if d.size()==0:
            print('-1')

    def MD(self,d,i):
        for j in range(d.size()-1,-1,-1):
            if d.items[j]>int(i):
                if(d.items[j]!=-99999):
                    v = ' Because ' + str(d.items[j]) +  ' is more than ' + i
                    print('Delete = '+str(d.items[j])+v)
                    
                d.items[j]=-99999
        if -99999 in d.items:
            d.items.remove(-99999)
        if d.size()==0:
            print('-1')
s = input('Enter Input : ')
d = Stack()
s = s.split(',')
for i in s:
    if len(i)!=1:
        i=i.split()
        if i[0]=="A" :
           Stack().A(d,i[1])
        elif i[0]=='D' :
            Stack().D(d,i[1])
        elif i[0]=='LD' :
            Stack().LD(d,i[1])
        elif i[0]=='MD' :
            Stack().MD(d,i[1])
    else:
        Stack().P(d)
print ( 'Value in Stack = ' +  '['+ ', '.join([str(e) for e in d.items if e !=-99999])  +']'  )
