def bubble_en(l):
    for i in range(len(l)-1,0,-1):
        for j in range(i):
            if l[j] > l[j+1] and l[j+1]>=0:
                l[j],l[j+1] = l[j+1],l[j] 
            elif  j<len(l)-2 and l[j] > l[j+2] and l[j+2]>=0:
                l[j],l[j+2] = l[j+2],l[j] 
    return l  

s = [int(e) for e in input('Enter Input : ').split()]

print(*bubble_en(s.copy()))