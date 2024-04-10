from heapq import heapify, heappop, heappush
def solution(jobs):
    startTimeHeap=[tuple(v) for v in jobs]
    heapify(startTimeHeap)
    workTimeHeap=[]
    
    time=0
    workTimeSum=0
    
    while(len(startTimeHeap) or len(workTimeHeap)):
        if len(startTimeHeap):
            if len(workTimeHeap)==0 or startTimeHeap[0][0]<=time:
                nearByWork = heappop(startTimeHeap)
                heappush(workTimeHeap, (nearByWork[1], nearByWork[0]))
                continue
        currWork=heappop(workTimeHeap)
        workTimeSum+=(currWork[0]+max(time, currWork[1])-currWork[1])
        time=max(time, currWork[1])+currWork[0]
        
    return workTimeSum//len(jobs)


        