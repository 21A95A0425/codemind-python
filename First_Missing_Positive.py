n=int(input())
k=list(map(int,input().split()))
for i in range(1,n+2):
    if i not in k:
        print(i)
        break
        