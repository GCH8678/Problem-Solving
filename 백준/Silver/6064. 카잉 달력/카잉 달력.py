# 자연수 x,y
# <x:y>

# 첫번 째 해 : <1:1>
# 두번 째 해 : <2:2>

# <x:y>의 다음해를 <x',y'>라 하자
# 만일 x<m 이면 x' = x+1
# 그렇지 않으면 x' = 1
# y<n 이면 y'=y+1, 아니면 1

# ex) M=10, n=12 => 1.<1:1> => 11번째 해 <1:11> => 13<3:1>
#                           => 60.<10,12>

# 마지막 해는 m과 n의 최소공배수
# M과 N이 카잉 달력의 마지막 해라고 하면 <x:y>는 몇번째 해인가?

import sys

def gcd(a,b):
    if a<b:
        a,b = b,a
    while b!=0:
        temp = a%b
        a = b
        b = temp
    return a

def lcm(a,b):
    return (a*b)//gcd(a,b)

#print(lcm(10,12))

#테스트 케이스 k
k = int(sys.stdin.readline())
for _ in range(k):
    m,n,x,y = map(int,sys.stdin.readline().split())
    k = -1
    
    for i in range(x,lcm(m,n)+1,m):
        tempY = i%n
        if tempY == 0:
            tempY = n
        if tempY == y:
            k=i
    print(k)