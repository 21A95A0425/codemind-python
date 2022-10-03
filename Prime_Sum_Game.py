a,b,c,d=map(int,input().split())
def check(z):
    i=2
    while i*i<=z:
        if not z%i:
            return False
        i+=1
    return True
def ch(z):
    i=c
    while i<=d:
        if check(z+i):
            return False
        i+=1
    return True
k=a
while k<=b:
    if ch(k):
        print("Takahashi")
        break
    k+=1
else:
    print("Aoki")