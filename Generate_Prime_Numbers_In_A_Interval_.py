def prime(n):
    
    if(n<=1):
         return False   
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return False
    return True
a=int(input())
b=int(input())
for n in range(a,b):
    if(prime(n)):
        print(n)
