
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

print(min_cnt)

