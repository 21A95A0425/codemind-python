z=int(input())
m=list(map(int,input().strip().split()))
s=0
avg=sum(m)//z
for i in m:
    if avg==i:
        print(True)
        break
if avg!=i:
    print(False)