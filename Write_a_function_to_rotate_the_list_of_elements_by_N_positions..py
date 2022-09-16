z=int(input())
m=list(map(int,input().split()))
a=int(input())
for i in range(a):
    b=m[z-1]
    m.pop()
    m.insert(0,b)
print(*m)