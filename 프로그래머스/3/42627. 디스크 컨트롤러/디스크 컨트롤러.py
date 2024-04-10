# from heapq import heapify, heappop, heappush
# import math
# def solution(jobs):
#     startTimeHeap=[tuple(v) for v in jobs]
#     heapify(startTimeHeap)
#     workTimeHeap=[]
    
#     time=0
#     workTimeSum=0
    
#     while(len(startTimeHeap) or len(workTimeHeap)):
#         if len(startTimeHeap):
#             if len(workTimeHeap)==0 or startTimeHeap[0][0]<=time:
#                 nearByWork = heappop(startTimeHeap)
#                 heappush(workTimeHeap, (nearByWork[1], nearByWork[0]))
#                 continue
#         currWork=heappop(workTimeHeap)
#         workTimeSum+=(currWork[0]+max(time, currWork[1])-currWork[1])
#         time=max(time, currWork[1])+currWork[0]
        
#     return math.floor(workTimeSum/len(jobs))


2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
import heapq
from collections import deque

def solution(jobs):
    tasks = deque(sorted([(x[1], x[0]) for x in jobs], key=lambda x: (x[1], x[0])))
    q = []
    heapq.heappush(q, tasks.popleft())
    current_time, total_response_time = 0, 0
    while len(q) > 0:
        dur, arr = heapq.heappop(q)
        current_time = max(current_time + dur, arr + dur)
        total_response_time += current_time - arr
        while len(tasks) > 0 and tasks[0][1] <= current_time:
            heapq.heappush(q, tasks.popleft())
        if len(tasks) > 0 and len(q) == 0:
            heapq.heappush(q, tasks.popleft())
    return total_response_time // len(jobs)

        