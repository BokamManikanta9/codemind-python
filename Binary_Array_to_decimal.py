n=int(input())
c=0
num=list(map(int,input().split()))
num.reverse()
for i in range(n):
    c=c+(num[i]*(2**i))
print(c)