n=int(input())
l=[]
arr=list(map(int,input().split()))
a,b=map(int,input().split())
for i in arr:
    if i>=a and i<=b:
        l.append(i)
if len(l)==0:
    print(-1)
else:
    print(min(l))