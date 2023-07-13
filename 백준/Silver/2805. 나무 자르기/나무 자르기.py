
import sys
# 나무 갯수 n
# 나무 길이 m (집에 가져가려는)

n,m = map(int,sys.stdin.readline().split())

lst = list(map(int,sys.stdin.readline().split()))

# M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이 최갯 값

# 절단기에 높이 H를 지정해야 -> 땅으로부터 h 미터 위로올라감
# 한줄에 연속해 있는 나무를 모두 절단
lst.sort()
#print(lst)


def check(mid,lst):
    # print("target",m)
    # print("mid",mid)
    # print("s e")
    sum = 0
    for i in lst:
        if i>=mid:
            sum+=i-mid
        #print(sum,i-mid)
        if sum>=m:
            #print("over",sum-m,"->",sum)
            return False
    #print(sum)
    return True
        

l,r = 0,max(lst)

while l+1<r:
    mid = (l+r)//2
    if (check(mid,lst)):
        r = mid
    else:
        l = mid

print(l)