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
            return 'empty'
        return self.data.pop(0)
    def size(self):
        return len(self.data)
    def top(self):
        if self.is_empty():
            return -1
        return self.data[0]

q = Queue()

s = input('Enter Input : ')
s = s.split(',')

for i in s:
    if len(i)!=1:
        v = i.split()
        if v[0]=='E':
            q.enqueue((v[1]))
            print(q.size())

        
        
    elif i[0]=='D':
        if(q.size()!=0):
            print(str(q.top())+" "+ '0')
        else :
            print('-1')
        q.dequeue()
if q.size()!=0:
    print(' '.join([e for e in q.data]))
else :
    print('Empty')