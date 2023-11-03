a,b=map(int,input().split())
l=[]
s=0
s1=0
for i in range(a):
    l.append(list(map(int,input().split())))
for i in range(a):
    for j in range(b):
        if i%2==0:
            s+=l[i][j]
        else:
            s1+=l[i][j]
print(s,end=' ')
print(s1)