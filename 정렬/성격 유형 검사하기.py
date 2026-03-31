def solution(survey, choices):
    answer = ''
    scores = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    
    for i in range(len(survey)):
        u, v = survey[i][0], survey[i][1] # u: 비동의 시 점수, v: 동의 시 점수
        choice = choices[i] 
        
        if choice > 4:
            scores[v] += (choice - 4)
        elif choice < 4: # 4(모름)일 때는 점수 변화가 없으므로 엄격하게 구분 가능
            scores[u] += (4 - choice)
            
    indicators = [("R", "T"), ("C", "F"), ("J", "M"), ("A", "N")]
    
    for c1, c2 in indicators:
        # 두 유형의 점수가 같을 경우 사전 순으로 빠른 c1이 선택되도록 설정됨
        if scores[c1] >= scores[c2]:
            answer += c1
        else:
            answer += c2
            
    return answer
