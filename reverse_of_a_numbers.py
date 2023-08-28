n=int(input())
q=n
rev=0
while q!=0:
    r=q%10
    rev=rev*10+r
    q=q//10
print(rev)