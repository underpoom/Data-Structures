class dic:
    def __init__(self,s):
        self.s = s
        self.d = [ord(e) for e in s if e.isalpha()][0]
    
def bubble_in(l):
    for i in range(len(l)-1,0,-1):
        for j in range(i):
            if l[j].d > l[j+1].d:
                l[j],l[j+1] = l[j+1],l[j]  
    return l

l = [dic(e) for e in input('Enter Input : ').split()]
print(*[e.s for e in bubble_in(l)])