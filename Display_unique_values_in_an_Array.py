a=int(input())
b=list(map(int,input().split()))
z=[]
for i in b:
    if b.count(i)==1:
        z.append(i)
if len(z)==0:
    print("-1")
else:
    print(*z)
    
       