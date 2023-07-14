# R은 배열에 있는 수의 순서를 뒤집는 함수
# D는 첫번째 수를 버리는 함수 -> 빈 배열에 사용시 에러 발생

# t : 테스트 케이스 갯수
# p : 함수 1<=p<=100,000
# n : 배열 길이 0<= n <= 100,000
# lst : [] 1<= len(lst) <= 100
import sys
import collections

t = int(sys.stdin.readline())
for _ in range(t):
    p = list(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    if n >0:
        lst = collections.deque(map(int,sys.stdin.readline().rstrip().lstrip("[").rstrip("]").split(",")))
    else:
        a = sys.stdin.readline()
        lst = []
    # print("n: ",n)
    # print("p: ",p)
    # print("lst: ",lst)

    sign = 1
    error = False
    for i in p:
        if i=="R":
            sign = sign*(-1)
        else :
            if lst:
                if 0<sign:
                    lst.popleft()
                else:
                    lst.pop()
            else:
                error = True
                break
    if error:
        print("error")
    else:
        print(str(list(lst)[::sign]).replace(" ",""))
            