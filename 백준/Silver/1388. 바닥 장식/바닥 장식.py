import sys
sys.setrecursionlimit(10**6)

row, col = list(map(int, input().split()))
floor=[list(input()) for _ in range(row)]
visited=[[0 for _ in range(col)] for _ in range(row)]

answer=0

def dfs(r, c, lastBoard, isSerching):
    global answer
        
    if r>=(row) or c>=(col): 
        if isSerching:
            answer+=1
        return
    
    if (isSerching and floor[r][c]!=lastBoard):
        answer+=1
        return
    curBoard=floor[r][c]

    if (curBoard==lastBoard or not isSerching) and visited[r][c]==False:
        visited[r][c]=True

        if curBoard=="-":
            dfs(r, c+1, "-", True)
        elif curBoard=="|":
            dfs(r+1, c, "|", True)
        if isSerching==True:
            return

    dfs(r+(c+1)//col, (c+1)%col, curBoard, False)


dfs(0, 0, floor[0][0], False)
print(answer)