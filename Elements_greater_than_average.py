n=int(input())
c=0
arr=list(map(int,input().split()))
x=sum(arr)//n
for i in arr:
    if i>=x:
        c+=1
print(c)