class Stack:
    def __init__(self):
        self.item = []
    def push(self,data):
        return self.item.append(data)
    def pop(self):
        return self.item.pop()
    def size(self):
        return len(self.item)
    def isEmpty(self):
        return self.size()==0
    def peek(self):
        if self.size()!=0:
            return self.item[-1]
    def __str__(self):
        return str(self.item)

    def D(self,data): #remove item that equaL data
        for i in range(self.size()-1,-1,-1):
            if self.item[i] == data:
                print('Delete =',str(self.item[i]))
                self.item.remove(self.item[i])
        if self.size()==0:
            return print('-1')

    def LD(self,data): #remove item that less than data
        for i in range(self.size()-1,-1,-1):
            if self.item[i] < data:
                print('Delete =',str(self.item[i]),'Because',str(self.item[i]),'is less than',data)
                self.item.remove(self.item[i])
        if self.size()==0:
            return print('-1')
            
    def MD(self,data): #remove item that more than data
        for i in range(self.size()-1,-1,-1):
            if self.item[i] > data:
                print('Delete =',str(self.item[i]),'Because',str(self.item[i]),'is more than',data)
                self.item.remove(self.item[i])
        if self.size()==0:
            return print('-1')
    
    def A(self,data):
        print('Add =',data)
        self.push(data)
    def P(self):
        if self.size()==0:
            return print('-1')
        print('Pop =',self.pop())

s = input('Enter Input : ')
st = Stack()
s = s.split(',')
for i in s:
    if len(i)!=1:
        i=i.split()
        i[1] = int(i[1])
        if i[0]=="A" :
           st.A(i[1])
        elif i[0]=='D' :
            st.D(i[1])
        elif i[0]=='LD' :
            st.LD(i[1])
        elif i[0]=='MD' :
            st.MD(i[1])
    else:
        st.P()
        
print('Value in Stack = [' + ', '.join([str(e) for e in st.item])+']')
