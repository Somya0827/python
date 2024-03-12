num=int(input("Enter a number : "))
sum=0
l=1

for i in range(1,num+1):
  l=num%10
  sum=sum+l
  num=num//10

print("sum of given digit is :",sum)
