z=int(input())
for i in range(1,z+1):
    m=int(input())
    a=str(m)
    b=a[::-1]
    c=int(b)
    if m==c:
        print(True)
    else:
        print(False)