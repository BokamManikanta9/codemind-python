n=int(input())
l=[]
arr=list(map(int,input().split()))
for i in arr:
    if i not in l:
        l.append(i)
for i in l:
    print(i,end=' ')