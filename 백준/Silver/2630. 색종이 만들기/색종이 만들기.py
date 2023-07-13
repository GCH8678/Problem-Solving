#[ny,nx]
#[i,j] -> [행,열] -> [세로,가로]

# n -> n//2 -> (n//2)//2 순으로 범위 축소

import sys

n = int(sys.stdin.readline())

lst = []

for _ in range(n):
    lst.append(list(map(int,sys.stdin.readline().split())))

def findBlue(square,offset,e):
    for i in range(e):
        for j in range(e):
            x = square[offset[0]+i][offset[1]+j]
            if x != 1:
                return False
    for i in range(e):
        for j in range(e):
            square[offset[0]+i][offset[1]+j] = 3
    return True

def findWhite(square,offset,e):
    for i in range(e):
        for j in range(e):
            x = square[offset[0]+i][offset[1]+j]
            if x != 0:
                return False
    for i in range(e):
        for j in range(e):
            square[offset[0]+i][offset[1]+j] = 3
    return True


cntB = 0
cntW = 0

x=0
while 2**x<=n:
    x+=1

e=n
for _ in range(x):
    #print(e)
    for i in range(n//e):
        for j in range(n//e):
            offset = [i*e,j*e]
            #print(offset)
            if findBlue(lst,offset,e):
                cntB+=1
            if findWhite(lst,offset,e):
                cntW+=1
    e //=2
print(cntW)
print(cntB)
