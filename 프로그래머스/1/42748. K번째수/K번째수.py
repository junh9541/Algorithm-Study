def solution(array, commands):
    answer = []
    for command in commands:
        newArr = array[command[0]-1:command[1]]
        newArr.sort()
        answer.append(newArr[command[2]-1])
    
    return answer