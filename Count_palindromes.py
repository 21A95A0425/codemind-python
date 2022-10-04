z=int(input())
m=list(map(int,input().split()))
s=0
for i in range(len(m)):
    a=m[i]
    b=str(a)
    c=b[::-1]
    if a==int(c):
        s+=1
print(s)