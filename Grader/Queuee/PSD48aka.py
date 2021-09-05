sn =[]
class Queue :
    def __init__(self) -> None:
        self.data = []
    def __str__(self) -> str:
        return str(self.data)
    def is_empty(self):
        return len(self.data) == 0
    def __len__(self):
        return len(self.data)
    def enqueue(self, new_data):
        return self.data.append(new_data)
    def dequeue(self):
        if self.is_empty():
            return 'Empty'
        return self.data.pop(0)
    def size(self):
        return len(self.data)
    def top(self):
        if self.is_empty():
            return -1
        return self.data[0]
    def fenqueue(self,idata):
      
       
        if idata in sn:
            for i in range(self.size()):
                if self.data[i] not in sn :
                    return self.data.insert(i,idata)
            return self.data.insert(self.size(),idata)
               
                    
        return self.data.insert(0,idata)

q = Queue()


s = input('Enter Input : ')
s = s.split(',')

for i in s:
    if i[0]=='E':
        v = i.split()
        if(v[0]=='EN'):
            q.enqueue((v[1]))
        elif(v[0]=='ES'):
            sn.append(v[1])
            q.fenqueue(v[1])
            
    
    elif i[0]=='D':
        if(q.size()!=0):
            print(str(q.top()))
        else :
            print('Empty')
        q.dequeue()
