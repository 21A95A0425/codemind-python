n=int(input())
m=list(map(int,input().strip().split()))[:n]
b=[]
for i in m:
    c=i*i
    b.append(c)
b.sort()
print(*b)