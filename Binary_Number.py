z=int(input())
b=2**z
for i in range(0,b):
    d=(bin(i)[2:])
    e=len(d)
    x=(z-e)*"0"
    print(x+d)