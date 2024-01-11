n=int(input())
arr=list(map(int,input().split()))
l=[]
for i in arr:
    if i not in l:
        print(i,arr.count(i),end=' ')
    l.append(i)