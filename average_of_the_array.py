z=int(input())
m=list(map(int,input().strip().split()))
s=0
#avg=sum(m)//z
for i in range(len(m)):
    s=s+m[i]
a=s/z
print("{:0.2f}".format(a))