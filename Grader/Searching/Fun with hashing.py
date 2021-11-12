class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:
    def __init__(self,data,sTable):
        data = data.split()
        self.data = Data(data[0],data[1])
        id = 0
        for i in data[0]:
            id+=ord(i)
        self.id = id%sTable
    def __str__(self):
        return str(self.data)
    
print(' ***** Fun with hashing *****')
s = input('Enter Input : ').split('/')
sTable ,mxCol ,empl = int(s[0].split()[0]),int(s[0].split()[1]),int(s[0].split()[0])
l = [None]*sTable
for i in s[1].split(','):
    k = hash(i,sTable)
    id = k.id
    nCol = 1
    while l[id] is not None and nCol <= mxCol:
        print('collision number',nCol,'at',id)
        id = (k.id+pow(nCol,2))%sTable
        nCol+=1
    if nCol-1 == mxCol:
        print('Max of collisionChain')
        for j in range(len(l)):
            print('#'+str(j+1)+'\t'+str(l[j]))
        print('---------------------------')
    if l[id] is None and nCol <= mxCol :
        l[id] = k
        empl-=1
        for j in range(len(l)):
            print('#'+str(j+1)+'\t'+str(l[j]))
        print('---------------------------')
    if empl == 0:
        print('This table is full !!!!!!')
        break
