z=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
s=0
b=[]
for i in a:
    if x<=i<=y:
        b.append(i)
print(sum(b))
#        s=1
#if s==1:
#    print(max(c))
#else:
#    print(-1)
