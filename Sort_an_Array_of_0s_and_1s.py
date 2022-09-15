n=int(input())
l=list(map(int,input().split()))
for i in range(len(l)):
    for j in range(i):
        if l[i]<l[j]:
            temp=l[i]
            l[i]=l[j]
            l[j]=temp
print(*l)
            