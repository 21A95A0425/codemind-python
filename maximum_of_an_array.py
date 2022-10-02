z=int(input())
m=list(map(int,input().strip().split()))
#s=0
a=[]
#avg=sum(m)//z
for i in range(len(m)):
    a.append(m[i])
print(max(a))    