a,b=map(int,input().split())
l=[]
for i in range(a):
    l.append(list(map(int,input().split())))
for i in l:
    print(sum(i),end=' ')