z=int(input())
m=int(input())
for i in range(z,m+1):
    a=str(i)
    b=a[::-1]
    c=int(b)
    if i==c:
        print(c,end=" ")