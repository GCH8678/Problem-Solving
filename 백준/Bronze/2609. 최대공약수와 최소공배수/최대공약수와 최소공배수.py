import sys
def gcd(a,b):
    while(b!=0):
        t=a%b
        (a,b)=(b,t)
    return a

a,b = map(int,sys.stdin.readline().split())


print(gcd(a,b))
print((a*b)//gcd(a,b))