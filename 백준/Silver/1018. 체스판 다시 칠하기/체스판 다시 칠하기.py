import sys

m,n = map(int,sys.stdin.readline().split())
arr = [input() for _ in range(m)] 

def countMin(i,j,arr,color):
    
    cnt = 0
    for k in range(8):
        for l in range(8):
            isEven = (k+l)%2== 0
            
            if isEven:
                if arr[j+l][i+k] == color:
                    cnt +=1
            else:
                if arr[j+l][i+k] != color:
                    cnt +=1
    return cnt


mn = 2500
for i in range(0,n-7):
    for j in range(0,m-7):
            
        mn = min(mn,countMin(i,j,arr,"W"),countMin(i,j,arr,"B"))

print(mn)
