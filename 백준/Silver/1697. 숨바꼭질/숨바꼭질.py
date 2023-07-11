import sys
from collections import deque
n,k = map(int,sys.stdin.readline().split())
q= deque([n])


check = [0]*100001

while q:
    v = q.popleft()
    if v == k:
        print(check[k])
        break

    lst = [v-1,v+1,2*v]
    for i in lst:
        if i>=len(check) or i<0:
            continue
        # check[n] 을 이후 들르게 되더라도 이후 노선을 이미 거쳐갔기 때문에 영향 없음
        if check[i] == 0:
            check[i] = check[v]+1
            q.append(i)