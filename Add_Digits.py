a=int(input())
s=0
if(a<10):
    print(a)
else:
    while(a>=10):
        n=a
        r=0
        while(n!=0):
            r += (n%10)
            n//=10
        if(r<10):
            print(r)
        a=r