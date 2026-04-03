def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    temp=""
    allowed = 'abcdefghijklmnopqrstuvwxyz0123456789_-.'
    for char in new_id:
        if char in allowed:
            temp +=(char)
            # 문자열은 append, pop 안되고 직접 넣어주면 됨
    new_id = temp
    
    # while을 쓸 수 있는지 고민해보자
    while ".." in new_id :
        new_id = new_id.replace('..' , '.')
        
    # 빈 문자열일 때도 고려해주어야 한다
    if len(new_id) >= 1:
        if new_id[0] == ".":
            new_id = new_id[1:]
    if len(new_id) >= 1:
        if new_id[-1] == ".":
            new_id = new_id[:-1]
        
    if len(new_id) == 0:
        new_id += "a"
        
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if len(new_id) >= 1:
            if new_id[0] == ".":
                new_id = new_id[1:]
        if len(new_id) >= 1:
            if new_id[-1] == ".":
                new_id = new_id[:-1]
        
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]
    answer= new_id
    print(new_id)
    return answer
