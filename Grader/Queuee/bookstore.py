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


ss = input('Enter Input : ')
ss = ss.split('/')
s1 = ss[0].split()
for i in s1:
    q.enqueue(int(i))
for i in ss[1].split(','):
    if i[0]=='E':
        v = i.split()
        q.enqueue(int(v[1]))
            
    
    elif i[0]=='D':
        q.dequeue()

l =[]
for i in q.data:
    if i not in l:
        l.append(i)
    else:
        print('Duplicate')
        break
if len(l) == q.size():
    print('NO Duplicate')