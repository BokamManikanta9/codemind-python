n=int(input())
arr=list(map(int,input().split()))
c=0
x=sum(arr)//n
for i in arr:
    if i<=x:
        c+=1
print(c)