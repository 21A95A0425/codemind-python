z=int(input())
m=list(map(int,input().strip().split()))
c=0
a=int(input())
#avg=sum(m)//z
for i in range(len(m)):
    if m[i]==a:
        c+=1
print(c)