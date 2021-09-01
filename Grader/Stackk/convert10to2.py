class Stack :
    v =[]
    def dec2bin(self,d):
        if d>1:
            Stack().dec2bin(d//2)
        return print(d%2,end='')

        


print(" ***Decimal to Binary use Stack***")

token = int(input("Enter decimal number : "))

print("Binary number : ",end='')

(Stack().dec2bin(token))