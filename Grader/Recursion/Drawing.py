def draw(n,i):
    if n==0:
        return print('Not Draw!')
    if n>i:
        print((n-i-1)*'_' + (i+1)*'#')
        draw(n,i+1)
    elif n<i:
        print(abs(i)*'_' + (i-n)*'#' )
        draw(n,i-1)
    if i==n:
        return
    
n = int(input('Enter Input : '))
draw(n,0)