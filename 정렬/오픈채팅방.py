def solution(record):
    answer = []
    dic = {}
    
    
    
    for i in record:
        log = i.split()
        command = log[0]
        id = log[1]
        
        
        # print(dic)
        
        if command == "Enter" or command == "Change":
            name = log[2]
            dic[id] = name
            # print(name)
            # 슬라이싱이 아니라 인덱스를 가져오면 그 안에 내용자체를 가져온다
        
    for i in record:
        log = i.split()
        id = log[1]
        command = log[0]
        if command == "Enter":
            answer.append(f"{dic[id]}님이 들어왔습니다.")
        if command == "Leave":
            answer.append(f"{dic[id]}님이 나갔습니다.")

    return answer
