print("*** Reading E-Book ***")
s,c = input("Text , Highlight : ").split(',')
for i in range(0,len(s)):
    if(c!=s[i]):
        print(s[i],end="")
    else:
        print("[",end="")
        print(s[i],end="")
        print("]",end="")