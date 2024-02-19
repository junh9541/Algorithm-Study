def solution(n, wires):
    answer = n
    for i in range(len(wires)):
        answer=min(checkWires(wires[:i]+wires[i+1:], n), answer)
    return answer

def checkWires(wires, n):
    checked=0
    nodesNum=len(set(sum(wires, [])))
    nodes=set([])
    if len(wires)==1:
        return 1
    for i in range(len(wires)):
        for j , wire in enumerate(wires):
            newNodes = nodes.union(wire)
            if len(newNodes)==2 or len(newNodes)-len(nodes)==1:
                nodes=newNodes
    
    return abs(n-len(nodes)* 2)
    
    
    