s=input()
k,m=1,1
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        k+=1
    else:
        k=1
    if k>m:
        m=k
print(m)