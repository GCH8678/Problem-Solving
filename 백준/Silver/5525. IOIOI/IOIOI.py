# n+1 개의 i와 n 개의 o로 이루어져 있으면
# I와 O가 교대로 나오는 문자열을 P_N 이라 한다

# 문자열 S와 정수 N 이 주어졌을 때, S안에 P_N이 몇군데 포함되어 있는지 구하는 프로그램을 작성하시오.

# 첫째 줄에 n이 주어진다. ( 둘째 줄에는 s의 길이 m이 주어짐)
# 셋째 줄에 S가 주어짐

import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()

pn = "I"+str("OI"*n)
# #print(pn,s)

# cnt = 0
# for i in range(m):
#     if pn[::] == s[i:i+n*2+1]:
#         cnt+=1

# print(cnt)

temp = "OI"

l,r=0,0
cnt =0
while l<m:
    if s[l:l+2*n+1] == pn:
        #print(s[l:l+2*n+1])
        cnt+=1
        r=l+2*n+1
        while s[r:r+2] == temp:
            #print(s[r:r+2])
            cnt+=1
            r+=2
        l=r
    else:
        l+=1
        #l = l+2*n
        #print(l)
print(cnt)