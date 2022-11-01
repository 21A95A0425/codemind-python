n=int(input())
z=list(map(int,input().strip().split()))[:n]
b=list(map(int,input().strip().split()))[:n]
for i in range(n):
    print(z[i]+b[i],end=' ')