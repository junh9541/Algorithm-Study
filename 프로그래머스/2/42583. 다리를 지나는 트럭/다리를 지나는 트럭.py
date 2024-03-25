from collections import deque
    
def solution(bridge_length, weight, truck_weights):
    remain=len(truck_weights)
    bridge=deque([])
    time=0
    truck=0
    bridgeSum=0
    while(remain):
        if len(bridge)==bridge_length:
            bridgeSum-=bridge.popleft()
        if bridgeSum+truck_weights[truck]<=weight:
            bridge.append(truck_weights[truck])
            bridgeSum+=truck_weights[truck]
            remain-=1
            truck+=1
        else:
            bridge.append(0)
        time+=1
    return time+bridge_length