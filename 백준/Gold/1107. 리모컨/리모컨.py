# 채널 N
# 고장난 버튼 갯수 M
# 고장난 버튼들

# 버튼: 0~9번 , +-
# 0 <= N <= 500,000
# 초기 채널 : 100

import sys
import itertools

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
brokenButton = []
if m>0:
    brokenButton = list(map(str,sys.stdin.readline().split()))
else:
    brokenButton = []
numpad = list()

min_cnt = abs(n-100)
for num in range(1000000):
    num = str(num)
    cnt = 0
    for j in num:
        if j in brokenButton:
            break
        else:
            cnt +=1
    if cnt == len(num):
        min_cnt = min(min_cnt,len(num)+abs(n-int(num)))

#print("dist",dist,"x",x)
print(min_cnt)

#현재 채널과 목표 채널이 채널글자수 보다 작거나 같으면 채널 돌리는게 더 빠르거나 비슷함
