from collections import Counter
z=int(input())
m=list(map(int,input().strip().split()))[:z]
a=[]
b=Counter(m)
c=0
for i in b:
    if m.count(i)==i:
        c+=1
print(c)
    