class translator:
    def deciToRoman(self, num):
        st = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        id = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        s =''
        for i in range(len(id)):
          while(num - id[i]>=0):
            s+=st[i]
            num-=id[i]
        return s
    def romanToDeci(self, s):
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        n=0
        for i in range(len(s)-1):
            if roman[s[i]] > roman[s[i+1]]:
                n+=roman[s[i]]
            else :
                n-=roman[s[i]]
        return n+roman[s[len(s)-1]]

n = int(input("Enter number to translate : "))
print(translator().deciToRoman(n))
print(translator().romanToDeci(translator().deciToRoman(n)))
