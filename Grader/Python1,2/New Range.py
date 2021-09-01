n = [float(e) for e in input('Enter Input : ').split()]
l = []
if len(n) == 1:
    x = 0.00
    while(x < n[0]):
       l.append(round(x,3))
       x+=1
if len(n) == 2:
    while(n[0] < n[1]):
       l.append(round(n[0],3))
       n[0]+=1
if len(n) == 3:
    while(n[0] < n[1]):
       l.append(round(n[0],3))
       n[0]+=n[2]

print( '(' + ', '.join([str(e) for e in l]) + ')')