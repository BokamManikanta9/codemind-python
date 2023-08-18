n=int(input())
s=0
p=1
q=n
while(q!=0):
    r=q%10
    s=s+r
    p=p*r
    q=q//10
if(s==p):
    print("Spy Number")
else:
    print("Not Spy Number")
