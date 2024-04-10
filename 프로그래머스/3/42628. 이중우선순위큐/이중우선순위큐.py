from heapq import heappop, heappush

def convertString(text):
    splitted = text.split()
    if splitted[0]=="D":
        return "max" if splitted[1]=="1" else "min"
    else:
        return int(splitted[1])
    
    
def solution(operations):
    maxHeap=[]
    minHeap=[]
    
    length = 0
    for text in operations:
        command = convertString(text)
        print(command)
        if length==0:
            maxHeap=[]
            minHeap=[]
        if command=="max":
            if length>0:
                heappop(maxHeap)
                length-=1
        elif command=="min":
            if length>0:
                heappop(minHeap)
                length-=1
        else:
            heappush(minHeap, command)
            heappush(maxHeap, (-command, command))
            length+=1
        print(minHeap, "|", maxHeap, "|", length)
    if length==0:
        return [0, 0]
    else:
        return [heappop(maxHeap)[1], heappop(minHeap)]

