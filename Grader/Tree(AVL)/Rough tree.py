s = input('Enter Input : ').split('/')
k = int(s[0])
l = [0]*(k+1)
node = [int(e) for e in s[1].split()]
ne = len(node)

if (k - ne)*2+1 == k:
    for i in range(ne):
        l[ne+i] = node[i]
    for i in range(k-ne,0,-1):
        d = min(l[i*2],l[i*2+1])
        l[i] = d
        l[i*2] -= d
        l[i*2+1] -=d
    print(sum(l))
else:
    print('Incorrect Input')