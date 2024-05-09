def solution(participant, completion):
    answer = ''
    setC=set(completion)
    dicC={name:0 for name in setC}
    for c in completion:
        dicC[c]=dicC[c]+1
    for p in participant:
        a=dicC.get(p, 0)
        if a<1:
            answer=p
            break
        dicC[p]=dicC[p]-1
    return answer
