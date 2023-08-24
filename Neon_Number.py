n=int(input())
s=0
x=n*n
q=x
while(q!=0):
    r=q%10
    s+=r
    q//=10
if(s==n):
    print("Neon Number")
else:
    print("Not Neon Number")