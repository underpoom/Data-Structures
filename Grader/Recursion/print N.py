def print1ToN(n):
    if n>1:
        print1ToN(n-1)
    else:
        return print(str(1),end=' ')
    print(str(n),end=' ')
def printNto1(n):
    if n>1:
        print(str(n),end=' ')
        printNto1(n-1)
    else :
        return print(str(1),end=' ')
  
n = int(input("Enter Input : "))
print1ToN(n)
printNto1(n)