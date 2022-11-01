n=int(input())
m=list(map(int,input().strip().split()))[:n]
ev,od=0,0
for i in range(len(m)):
    if i%2==0:
        ev=ev+m[i]
    else:
        od=od+m[i]
dif=ev-od
if dif==0:
    print('YES')
else:
    print('NO')