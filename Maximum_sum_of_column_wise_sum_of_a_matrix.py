z,m=map(int,input().split())
s=[0]*(m)
for i in range(z):
    m=list(map(int,input().split()))
#    b.append(sum(a))
    for j in range(len(m)):
        s[j]+=m[j]
print(max(s))