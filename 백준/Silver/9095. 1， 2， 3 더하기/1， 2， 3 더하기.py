# 1,2,3의 합으로 나타내는 방법의 가짓 수

# t : 테스트 케이스 수
# n : 1,2,3의 합으로 만들어야 하는 값
# 1<= n <= 10

import sys
from collections import deque

t = int(sys.stdin.readline())

e = [3,2,1]

for _ in range(t):
    n = int(sys.stdin.readline())
    q = deque([1,2,3])
    cnt = 0
    while q:
        #print(q)
        node = q.popleft()
        if node ==n:
            cnt+=1
        if node < n:
            for i in e:
                q.append(node+i)
    print(cnt)