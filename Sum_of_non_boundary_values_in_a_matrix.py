z,m=map(int,input().split())
s=0
for j in range(z):
    m=list(map(int,input().split()))
    for i in range(len(m)):
        if j!=0 and j!=(z-1):
            if i!=0 and i!=len(m)-1:
                s+=m[i]
print(s)
    