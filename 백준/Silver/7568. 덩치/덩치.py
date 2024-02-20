import heapq

#입력받기
n=int(input())
bodyData = []
for i in range(n):
    inputData = list(map(int, input().split()))  
    bodyData.append(inputData)


score = [0 for i in range(n)]
ranking = [0 for i in range(n)]

#몸무게, 키 비교
for  i, a in enumerate(bodyData[:-1]):
    for j, b in enumerate(bodyData[i+1:]):
        if a[0]>b[0] and a[1]>b[1]:
            score[j+i+1]+=1
        elif b[0]>a[0] and b[1]>a[1]:
            score[i]+=1

#점수와 인덱스 힙에 넣기
heap = []
for i in range(n):
    heapq.heappush(heap, (score[i], i))


#힙에서  적게 진 사람부터 꺼내기
#꺼낸 순서대로 ranking에 등수 기록
for i in range(1, n+1):
    data = heapq.heappop(heap)
    ranking[data[1]]=data[0]+1


result = " ".join(str(s) for s in ranking)
print(result)
