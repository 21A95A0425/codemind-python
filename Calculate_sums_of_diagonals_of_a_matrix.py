z=int(input())
s=0
a=0
for i in range(z):
    m=list(map(int,input().split()))
    s+=m[i]
    a+=m[z-1-i]
print("Principal Diagonal:",end="")
print(s)
print("Secondary Diagonal:",end="")
print(a)