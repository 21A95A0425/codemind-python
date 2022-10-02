z=int(input())
m=list(map(int,input().strip().split()))[:z]
ev=0
od=0
for i in range(len(m)):
    if m[i]%2==0:
        ev+=1
    else:
        od+=1
print(ev,od)