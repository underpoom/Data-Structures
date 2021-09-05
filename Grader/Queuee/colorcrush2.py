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
    def threedequeue(self):
        for i in range(3):
            self.data.pop(self.size()-1)
    def c_topthree(self,x):
        if x.data[-1]==x.data[-2] and x.data[-2]==x.data[-3]:
            return True
        return False
m_ex = 0
cbqt = Queue()
s = input('Enter Input (Normal, Mirror) : ').split()
qt,bqt = Queue(),Queue()
s[1] = s[1][::-1]
for i in s[1]:
    qt.enqueue(i)
    if qt.size()>=3:
        if Queue().c_topthree(qt):
            bqt.enqueue(qt.data[-1])
            cbqt.enqueue(qt.data[-1])
            qt.threedequeue() 
            m_ex+=1
normal_ex = 0
bqt_ex = 0
q = Queue()
for i in s[0]:
    q.enqueue(i)
    if q.size()>=3:
        if Queue().c_topthree(q):
            if bqt.size()!=0:
                q.data.insert(q.size()-1,bqt.top())
                bqt.dequeue()
        if Queue().c_topthree(q):
            if q.data[q.size()-1] in cbqt.data:
                cbqt.dequeue()
                bqt_ex+=1
            else:
                normal_ex+=1
            q.threedequeue() 
s = ''.join([e for e in q.data])
print('NORMAL :')
print(len(s))
if len(s)!=0:
    print(s[::-1])
else:
    print('Empty')
print(str(normal_ex) + ' Explosive(s) ! ! ! (NORMAL)')
if bqt_ex!=0:
    print('Failed Interrupted '+ str(bqt_ex)+' Bomb(s)')
print('------------MIRROR------------')
print(': RORRIM')
print(qt.size())
if qt.size()!=0:    
    print(''.join([str(e) for e in qt.data][::-1]))
else:
    print('ytpmE')
print('(RORRIM) ! ! ! (s)evisolpxE '+str(m_ex))