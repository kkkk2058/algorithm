def solution(id_list, report, k):
    answer = []
    answer_dic = {}
    reported_dic = {}
    result=[]
    report = set(report)
    for user in id_list:
        answer_dic[user] = 0
    # 한줄로 딕셔너리 넣기
    reported_dic = {user: 0 for user in id_list}
    
    # report 안에 내용을 2분류로 나누기 위한 방법
    for i in report:
        reporter, reported = i.split(" ")
        reported_dic[reported] +=1
        
    print(reported_dic)
    
    for i in report:
        reporter, reported = i.split(" ")
        if reported_dic[reported] >=k:
            answer_dic[reporter] +=1
    
    print(answer_dic)
    
    
    for k in id_list:
        # user 를 넣어야되므로 반복문안에 있는 k 를 인자로 넣어주어야 한다
        result.append(answer_dic[k])
    answer = result
    return answer
