z=int(input())
m=list(map(int,input().strip().split()))[:z]
if z>1:
    for i in range(1,z//2+1):
        print(m[i-1],m[z-i],end=" ")
    if z%2:
        print(m[i],0)
else:
    print(m[0],0)