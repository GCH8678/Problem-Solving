import sys
n1 = int(sys.stdin.readline().rstrip())
m1 = list(map(int,sys.stdin.readline().rstrip().split()))

n2 = int(sys.stdin.readline().rstrip())
m2 = list(map(int,sys.stdin.readline().rstrip().split()))

m1.sort()

lst = [0 for _ in range(n2)]

for keyIdx in range(n2):
    low=0
    high=n1-1
    while low<=high:
        mid = low+(high-low)//2
        if m1[mid] == m2[keyIdx]: 
            lst[keyIdx]=1
            break
        elif m1[mid]>m2[keyIdx]:
            high = mid-1
        else:
            low = mid+1
for i in lst:
    print(i)