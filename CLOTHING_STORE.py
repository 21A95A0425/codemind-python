a=int(input())
b=list(map(int,input().split()))
c=set(b)
z=0
for i in c:
    d=b.count(i)
    z+=d//2
print(z)