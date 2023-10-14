n=int(input())
c=0
num=list(map(int,input().split()))
for i in num:
    if i%2==0:
        c+=1
if c==n:
    print("True")
else:
    print("False")