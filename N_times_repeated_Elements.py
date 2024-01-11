n=int(input())
l=[]
c=0
arr=list(map(int,input().split()))
k=int(input())
for i in arr:
    if arr.count(i)==k and i not in l:
        print(i,end=' ')
        l.append(i)
    else:
        c+=1
if c==len(arr):
    print("-1")