def bubble_de(l):
    for i in range(len(l)-1,0,-1):
        for j in range(i):
            if l[j] < l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]  
    return l  

def bubble_in(l):
    for i in range(len(l)-1,0,-1):
        for j in range(i):
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]  
    return l

def check(l):
    lc = []
    for i in l:
        if i not in lc:
            lc.append(i) 
    not_dup = l == lc
   
    if l.count(l[0]) == len(l):
        return "Repdrome"
    elif l == bubble_in(l.copy()) and not_dup:
        return  "Metadrome"
    elif l == bubble_in(l.copy()):
        return "Plaindrome"
    elif l == bubble_de(l.copy()) and not_dup:
        return "Katadrome"
    elif l == bubble_de(l.copy()):
        return "Nialpdrome"
    else:
        return  "Nondrome"

s = [int(e) for e in input('Enter Input : ')]
print(check(s))