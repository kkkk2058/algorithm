import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    dic = {}
    queue = deque()
    for i in range(len(progresses)):
        
        dic[progresses[i]] = speeds[i]
    
        # day = (100-progresses[i]) / speeds[i]
        day = math.ceil((100-progresses[i]) / speeds[i])
        queue.append(day)
        # print(queue)
        
        
        
    while queue:
        count = 0
        standard = queue.popleft()
        count+=1
        while queue and queue[0] <= standard:
            queue.popleft()
            count+=1
            
        answer.append(count)
            
            
    return answer
