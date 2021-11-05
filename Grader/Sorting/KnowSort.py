def bubble(l):
    for i in range(len(l)-1,0,-1):
        for j in range(i):
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1],l[j] 
    return l  

s = [int(e) for e in input('Enter Input : ').split()]

print('Yes' if bubble(s.copy()) == s else 'No')