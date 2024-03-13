
def dsf(start, end, preyList, target):
    if start==end or end<start:
        if preyList[start]<target:
            return start+1
        else:
            return start
    
    if preyList[(start+end)//2]<target:
        return dsf((start+end)//2+1, end, preyList, target)
    else:
        return dsf(start, (start+end)//2-1, preyList, target)

testNum=int(input())
predators=[]
preys=[]
fishNum=[]
for i in range(testNum):
    fishNum.append(list(map(int, input().split())))
    predators.append(list(map(int, input().split())))
    prey=list(map(int, input().split()))
    prey.sort()
    preys.append(prey)

for test in range(testNum):
    sum=0
    for target in predators[test]:
        sum+=dsf(0, len(preys[test])-1, preys[test], target)
    print(sum)