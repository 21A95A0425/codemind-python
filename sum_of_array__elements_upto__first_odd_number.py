z=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    if i%2==0:
        s=s+i
    if i%2==1:
        break
print(s)
