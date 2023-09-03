n=int(input())
for i in range(1,n+1):
    s=int(input())
    c=int(s**0.5)
    j=c*c
    if j==s:
        print("True")
    else:
        print("False")
        c=0
        s=0