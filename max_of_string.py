a=list(input())
c=[]
for i in a:
    c+=[ord(i)]
print(chr(max(c)))