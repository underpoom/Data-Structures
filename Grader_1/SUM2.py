s = [int(e) for e in input('Enter Your List : ').split()]
l = []
d = [0]*3
for i in range(0,len(s)):
  for j in range(i+1,len(s)):
    for k in range(j+1,len(s)):
      if s[i]+s[j]+s[k] ==5:
        d[0] = s[i]
        d[1] = s[j]
        d[2] = s[k]
        d.sort()
        if d not in l:
          l.append(d.copy())

print('Array Input Length Must More Than '+ str(len(s))) if len(s)<=3 else print(l)

