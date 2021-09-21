def p(a,n):
    if n==0:
        return 1
    return a*p(a,n-1)
s = input('Enter Input a b : ').split()
print(p(int(s[0]),int(s[1])))