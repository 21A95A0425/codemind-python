z=int(input())
m=list(map(int,input().strip().split()))
s=0
#a=[]
#avg=sum(m)//z
for i in range(len(m)):
    if m[i]%2==0:
        a=s
    s+=1
print(a)