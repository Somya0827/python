sample_list=['p','q']
n=int(input("Enter number:"))

def concat(sample_list,n):
  l=[]
  for i in range(1,n+1):
    for j in sample_list:
      temp=j+str(i) 
      l.append(temp)
  return l
p=concat(sample_list,n)
print(p)
