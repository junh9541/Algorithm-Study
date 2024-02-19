def solution(elements):
    answer = set([])
    elementsSize = len(elements)
    for i in range(elementsSize):
        result=0
        for j in range(elementsSize):
            result+=elements[(i+j)%elementsSize]
            answer.add(result)

    return len(answer)
