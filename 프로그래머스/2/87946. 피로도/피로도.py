answer=0
visited=[]
def solution(k, dungeons):
    global visited
    global answer

    visited=[0 for i in range(len(dungeons))]
    permutation(0, k, dungeons)
    return answer
    
#순열 재귀
def permutation(count, k, dungeons):
    global answer
# 조건 1: count가 answer보다 클 때
    if count>answer:
        answer=count
    for i in range(len(dungeons)):
        if not visited[i] and k>=dungeons[i][0]:
            visited[i]=True
            permutation(count+1, k-dungeons[i][1], dungeons)
            visited[i]=False