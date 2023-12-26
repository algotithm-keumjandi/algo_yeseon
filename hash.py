def solution(participant, completion):
    part={}
    comp={}
    pvar = 0

    for i in participant:
        # 해시로 딕셔너리화 
        part[i] = hash(i)
        pvar += hash(i)
        
    for j in completion:    
        comp[j] = hash(j)
        pvar -= comp[j]

    for i in part: 
        if (part[i] == pvar):
            return i