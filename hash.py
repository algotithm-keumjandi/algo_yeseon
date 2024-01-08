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
        
#         정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.1MB)
# 테스트 3 〉	통과 (0.27ms, 10.4MB)
# 테스트 4 〉	통과 (0.58ms, 10.4MB)
# 테스트 5 〉	통과 (0.52ms, 10.6MB)
# 테스트 6 〉	통과 (0.00ms, 10.1MB)
# 테스트 7 〉	통과 (0.00ms, 10.3MB)
# 효율성  테스트
# 테스트 1 〉	통과 (29.73ms, 28.2MB)
# 테스트 2 〉	통과 (48.03ms, 33.7MB)
# 테스트 3 〉	통과 (57.29ms, 37.5MB)
# 테스트 4 〉	통과 (62.52ms, 46.9MB)
# 테스트 5 〉	통과 (66.75ms, 46.8MB)
# 채점 결과
# 정확성: 58.3
# 효율성: 41.7
# 합계: 100.0 / 100.0