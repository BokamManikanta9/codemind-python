n=int(input())
c=0
l=[]
arr=list(map(int,input().split()))
for i in arr:
    if i%2!=0 and i not in l:
        c+=1
        l.append(i)
print(c)