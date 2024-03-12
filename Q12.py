first=0
second=1
n=int(input("upto how many terms:"))
print(first)
print(second)
for i in range(1,n-1):
  third=first+second
  print(third)
  first=second
  second=third
