def factorial(n):
  if(n==1):
    return 1
  else:
    return n*factorial(n-1)
  
num=int(input("enter number:"))
if(num<0):
  print("factorial does not exist")
elif(num==0):
  print("the factorial of 0 is 1")
else:
  print("The factorial of",num,"is",factorial(num))