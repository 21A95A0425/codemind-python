a=int(input())
p=int(input())
for i in range(1,p+1):
    w,h=map(int,input().split())
    if w==h>=a:
        print("ACCEPTED")
        continue
    else:
        if w<a or h<a:
            print("UPLOAD ANOTHER")
            continue
        else:
            print("CROP IT")
            continue
