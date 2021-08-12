print('*** multiplication or sum ***')
a,b = (int(e) for e in input('nEnter num1 num2 : ').split())
print("The result is",a+b)  if(a*b>1000) else  print("The result is",a*b)
