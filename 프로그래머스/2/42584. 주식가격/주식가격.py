from collections import deque

def solution(prices):
    MAX=100*1000+1
    answer = [0 for _ in range(len(prices))]
    stackPrices=deque([])
    
    for i in range(len(prices)):
        if not(len(stackPrices)):
            stackPrices.append(prices[i])
        elif stackPrices[-1]<=prices[i]:
            stackPrices.append(prices[i])
        elif stackPrices[-1]>prices[i]:
            time=0
            while(len(stackPrices)):
                if stackPrices[-1]>prices[i]:
                    time+=1
                    if stackPrices.pop()!=MAX:
                        answer[i-time]=time 
                else:
                    break
            stackPrices.extend([MAX for _ in range(time)]+[prices[i]])

    time=0
    while len(stackPrices):
        if stackPrices.pop()!=MAX:
            answer[-1-time]=time
        time+=1
                
        
        
        
    
    
    return answer