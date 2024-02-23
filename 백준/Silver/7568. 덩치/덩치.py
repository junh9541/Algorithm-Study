n=int(input())
bodyData = []
for i in range(n):
    inputData = list(map(int, input().split()))  
    bodyData.append(inputData)


ranking = [0 for i in range(n)]

#몸무게, 키 비교
for  i, a in enumerate(bodyData[:-1]):
    for j, b in enumerate(bodyData[i+1:]):
        if a[0]>b[0] and a[1]>b[1]:
            ranking[j+i+1]+=1
        elif b[0]>a[0] and b[1]>a[1]:
            ranking[i]+=1


for i in range(n):
    ranking[i]+=1


result = " ".join(str(s) for s in ranking)
print(result)
