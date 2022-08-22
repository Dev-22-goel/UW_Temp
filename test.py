import math

def isPerfect(x):
    if (x>=0):
        sr=int(math.sqrt(x))
        return ((sr*sr)==x)
    return False


def canReach(c, x1, y1, x2, y2):
    # Write your code here
    k=max(x1,y1,x2,y2)
    
    d= [[0 for i in range (k+1)] for j in range (k+1)]
    d[x1][y1]=1
    
    for i in range(x1, k+1):
        for j in range (y1, k+1):
            if isPerfect(i+j)or (i==x1 and j==y1):
                continue
            
            elif (i-c)>-1 and (j-c)>-1 and d[i-c][j-c]==1:
                d[i][j]==1
                
            elif d[i-j][j]==1 or d[i][j-i]==1:
                d[i][j]==1
    
    if d[x2][y2]==1:
        return "Yes"
    
    return "No"

print(canReach(1,1,4,7,6))