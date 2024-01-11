n=int(input())
c=0
l=[]
arr=list(map(int,input().split()))
for i in arr:
    if arr.count(i)==i:
        l.append(i)
l=list(l)
l=set(l)
print(len(l))