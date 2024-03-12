num=int(input("enter no of row you want:"))
n=1
for i in range(1,num+1): #i for row
  for j in range(1,i+1): #j for column
    print(n,end=" ")
    n=n+1
  print()
