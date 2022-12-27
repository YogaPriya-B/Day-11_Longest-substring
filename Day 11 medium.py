s=input()

l1=[]

a=0
for i in range(0,len(s)+1):
    for j in range(i+1,len(s)+1):
      
        l1.append(s[i:j])
k=int(input())
l=[]
for m in l1:
    n=set(m)
    if(len(n)==k):
        l.append(m)
if(l==[]):
    print("Not enough unique characters")
else:
  res=max(l,key=len)
  print(res)
