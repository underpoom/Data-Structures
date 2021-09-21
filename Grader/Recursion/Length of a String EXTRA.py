def _l(s,i):
    if s=='':
        return print('\n'+str(i))
    print(s[0],end='*') if i%2==0 else print(s[0],end='~')
    _l(s[1:],i+1)
s = input('Enter Input : ')
i = _l(s,0)