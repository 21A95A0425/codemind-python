a=int(input())
b=list(map(int,input().split()))
for i in b:
    if b.count(i)>(a/2):
        print(i)
        break