s = input('Enter String and Number of Function : ').split()
st = s[0]
n = int(s[1])
if n == 1:
  print(len(st))
elif n == 2:
  print(st.swapcase())
elif n == 3:
  print(st[::-1])
else:
  l = []
  for i in s[0]:
    if i not in l:
        print(i,end='')
        l.append(i)
