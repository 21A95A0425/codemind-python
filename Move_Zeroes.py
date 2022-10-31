a=int(input())
b=list(map(int,input().split()))
c,d=[],[]
for i in b:
    if i==0:
        c.append(0)
    if i!=0:
        d.append(i)
print(*d+c)

        
