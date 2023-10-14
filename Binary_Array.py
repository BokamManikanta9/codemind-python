n=int(input())
c=0
num=list(map(int,input().split()))
for i in num:
    if i==0 or i==1:
        c+=1
if c==n:
    print("True")
else:
    print("False")