def solution(answers):
    
    p1=[1, 2, 3, 4, 5]
    p2=[2, 1, 2, 3, 2, 4, 2, 5]
    p3=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    score=[0, 0, 0]
    
    for i, elem in enumerate(answers):
        if p1[i%5]==elem:
            score[0]+=1
        if p2[i%8]==elem:
            score[1]+=1
        if p3[i%10]==elem:
            score[2]+=1
            
    answer = []
    
    maxSc=max(score)
    for i in range(0, 3):
        if score[i]==maxSc:
            answer.append(i+1)

    return answer