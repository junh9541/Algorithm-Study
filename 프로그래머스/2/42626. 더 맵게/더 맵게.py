import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    time = 0
    while(scoville[0]<K):
        if len(scoville)<2:
            return -1
        heapq.heappush(scoville, heapq.heappop(scoville)+heapq.heappop(scoville)*2)
        time+=1
    return time