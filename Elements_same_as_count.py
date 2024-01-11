n=int(input())
c=0
l=[]
arr=list(map(int,input().split()))
for i in arr:
    if arr.count(i)==i and i not in l:
        l.append(i)
    else:
        c+=1
if c==len(arr):
    print("-1")
else:
    print(*l)