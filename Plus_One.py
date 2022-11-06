a=int(input())
b=list(map(int,input().split()))
z=[]
c=''
for i in b:
    i=str(i)
    c+=i
c=int(c)
c+=1
c=str(c)
for i in c:
    z.append(i)
print(*z)