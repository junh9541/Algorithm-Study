def dfs(node):
    visited[node]=True
    for next in bridges[node]:
        if visited[next]==True:
            continue
        dfs(next)


computerNum=int(input())
bridgeNum=int(input())

bridges=[[] for _ in range(computerNum+1)]
visited=[0 for _ in range(computerNum+1)]

for i in range(bridgeNum):
    start, end = list(map(int, input().split()))
    bridges[start].append(end)
    bridges[end].append(start)


dfs(1)
print(sum(visited)-1)