#입력 데이터의 수 : T
# 각 테스트 데이터 첫째 줄에는 Q에 적용할 연산의 갯수 k
# k<= 1,000,000
# 그 뒤 k의 줄 동안 D,I와 정수 n 이 주어짐
# I n : 정수 n을 Q에 삽입
# D 1 : Q에서 최댓값을 삭제함을 의미
# D -1 : Q에서 최소값을 삭제함을 의미

import sys
import heapq


t = int(sys.stdin.readline())

def solution(k):
    minheap =[]
    maxheap =[]
    trash = [False]*k
    for i in range(k):
        fn,n = map(str,sys.stdin.readline().split())
        n = int(n)
        if fn == "I":
            heapq.heappush(minheap,(n,i))
            heapq.heappush(maxheap,(-n,i))
        elif fn == "D":
            if maxheap and n == 1:
                dlt = heapq.heappop(maxheap)
                trash[dlt[1]] = True
            elif minheap and n == -1:
                dlt = heapq.heappop(minheap)
                trash[dlt[1]] = True
            while minheap and trash[minheap[0][1]]:
                heapq.heappop(minheap)
            while maxheap and trash[maxheap[0][1]]:
                heapq.heappop(maxheap)

    # while minheap and trash[minheap[0][1]]:
    #     heapq.heappop(minheap)
    # while maxheap and trash[maxheap[0][1]]:
    #     heapq.heappop(maxheap)

    if minheap and maxheap:
        print(*[-maxheap[0][0],minheap[0][0]])    
    else:
        print("EMPTY")
#출력 : Q에 남아있는 값중 최댓값과 최소값을 출력하라

for _ in range(t):
    k = int(sys.stdin.readline()) 
    solution(k)
