a,b=map(int,input().split())
l=[]
s=0
s1=0
for i in range(a):
    l.append(list(map(int,input().split())))
for i in l:
    for j in i:
        s+=j
print(s)