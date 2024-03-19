def solution(n, times):
    
    times.sort()
    
    minN=times[0]*(n//len(times))
    maxN=times[-1]*(n//len(times)+n%len(times))
    remain=n
    answer=maxN
    while(minN<=maxN ):
        half=(minN+maxN)//2

        for casher in times:
            remain-=half//casher

        if remain>0:
            minN=half+1
            flag=False
        else: 
            answer=min(half, answer)
            maxN=half-1
            flag=True
        remain=n
    return answer