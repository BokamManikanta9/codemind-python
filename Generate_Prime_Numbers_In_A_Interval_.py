a=int(input())
b=int(input())
if a==1:
    a=2
    for i in range(a,b):
        c=0
        for j in range(2,i):
            if i%j==0:
                c=1
                break
        if c==0:
                print(i)
else:
    for i in range(a,b):
        c=0
        for j in range(2,i):
            if i%j==0:
                c=1
                break
        if c==0:
                print(i)
