n=int(input())
arr=list(map(int,input().split()))
l=[]
c=0
for i in arr:
    if arr.count(i)==i and i not in l:
        l.append(i)
    else:
        c+=1
if c==len(arr):
    print("-1")
else:
    print(min(l),max(l))