import heapq

def solution(people, limit):
    answer=0
    queue=[]
    people.sort()
    
    for i in range(len(people)-1, -1, -1):
        if len(queue)==0:
            queue.append(people[i])
            continue

        if queue[-1]+people[i]<=limit:            
            queue.pop()
            answer+=1
        else:
            queue.append(people[i])
                        
    answer+=len(queue)
    return answer