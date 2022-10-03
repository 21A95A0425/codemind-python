z=int(input())
x=list(map(int,input().split()))
c=0
for i in x:
    c^=i
print(c)