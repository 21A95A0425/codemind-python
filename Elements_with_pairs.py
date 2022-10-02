z=int(input())
m=list(map(int,input().strip().split()))[:z]
a=[]
s=0
if len(m)%2:
    for i in range(len(m)):
        print(m[i],end=" ")
    print(0)
else:
    for i in range(len(m)):
        print(m[i],end=" ")
