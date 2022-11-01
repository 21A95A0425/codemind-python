n=int(input())
m=list(map(int, input().split()))
c,s=0,0
for i in m:
    if i==1: 
        c+=1
    if c>s:
        s=c
    if i!=1:
        c=0
print(s)