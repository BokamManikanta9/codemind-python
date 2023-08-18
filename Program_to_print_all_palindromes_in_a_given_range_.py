def palindrome(k,rev):
    q=k
    while(q!=0):
        r=q%10
        rev=rev*10+r
        q=q//10
    return rev==k
a=int(input())
b=int(input())
rev=0
for n in range(a,b+1):
    if(palindrome(n,rev)):
        print(n,end=" ")
    
