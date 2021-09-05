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
            return 'Empty'
        return self.data[0]

    def fenqueue(self,l,idata):     
        for i in range(self.size()-1,-1,-1):
            if Queue.croom(l,self.data[i],idata) == True:
                return self.data.insert(i+1,idata)
        return self.data.append(idata)
    def croom(l,a,b):
        for i in range(len(l)):
          if a in l[i] and b in l[i]:
                return True
        return False

q = Queue()
l =[[] for i in range(99999)]

ss = input('Enter Input : ')
ss = ss.split('/')

for i in ss[0].split(','):
    i = i.split()
    l[int(i[0])].append(i[1])

for i in ss[1].split(','):
    if i[0]=='E':
        v = i.split()
        q.fenqueue(l,v[1])
    elif i[0]=='D':
        print(q.top())
        q.dequeue()