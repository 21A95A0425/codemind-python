z=int(input())
m=list(map(int,input().strip().split()))
a=[]
for i in range(len(m)):
    if m[i] not in a:
        print(m[i],end=" ")
    a.append(m[i])