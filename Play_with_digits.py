z=int(input())
m=list(map(int,input().split()))
s=0
for i in range(len(m)):
    a=m[i]
    while a!=0:
        r=a%10
        s+=r
        a=a//10
print(s)