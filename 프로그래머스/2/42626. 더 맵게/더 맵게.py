import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    time = 0
    while(scoville[0]<K and len(scoville)>=2):
        heapq.heappush(scoville, heapq.heappop(scoville)+heapq.heappop(scoville)*2)
        time+=1
    if scoville[0]>=K:
        return time
    else:
        return -1