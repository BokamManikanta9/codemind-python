n=int(input())
cn=0
a=0
b=1
for i in range(n):
    c=a+b
    if c==n:
        cn+=1
    a=b
    b=c
if cn!=0:
    print("True")
else:
    print("False")