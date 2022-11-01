n=int(input())
m=list(map(int,input().strip().split()))[:n]
a=int(input())
big,c=max(m),[]
for i in range(len(m)):
    if (m[i]+a)>=big:
        c.append(True)
    else:
        c.append(False)
print(*c)