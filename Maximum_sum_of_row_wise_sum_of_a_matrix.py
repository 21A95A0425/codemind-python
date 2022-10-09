z,m=map(int,input().split())
s=0
a=[]
for i in range(z):
    m=list(map(int,input().split()))
#    b.append(sum(a))
    for j in range(len(m)):
        s+=m[j]
    a.append(s)
    s=0
print(max(a))