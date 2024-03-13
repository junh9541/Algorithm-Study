
def dfs(start, end, target):
    if numbers[(start+end)//2]==target:
        return 1
    if start==end or start<0 or end<0 or start>end:
        return 0
    
    if numbers[(start+end)//2]>target:
        return dfs(start, (start+end)//2-1, target)
    else:
        return dfs((start+end)//2+1, end, target)
    
n=int(input())
numbers=list(map(int, input().split()))
numbers.sort()

n2=int(input())
targets=list(map(int, input().split()))

for v in targets:
    print(dfs(0, len(numbers)-1, v))
    