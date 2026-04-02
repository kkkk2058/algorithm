import math

def solution(today, terms, privacies):
    answer = []
    date = []
    year, month, day = map(int,today.split("."))
    today = year*28*12 + month*28 + day
    terms_dict = {}
    for t in terms:
        type, number = t.split(" ")
        terms_dict[type] = int(number) *28
    
    print(terms_dict)
    for i in range(len(privacies)):
#         p_date, p_type = map(int, privacies[i].split(" "))
# 동작 방식: split(" ")을 하면 ["2021.05.02", "A"]라는 리스트가 생깁니다. 그 다음 map(int, ...)가 이 리스트의 모든 요소를 **숫자(int)**로 바꾸려고 시도합니다.

# 문제점: "2021.05.02"는 점(.)이 들어있어서 숫자로 바로 바꿀 수 없고, 무엇보다 "A"는 알파벳이라 숫자로 바꿀 수 없습니다.

# 결과: ValueError: invalid literal for int() with base 10: '2021.05.02' 또는 'A' 에러가 나며 튕깁니다.
        
        p_split = privacies[i].split(" ")
        p_date = p_split[0]
        p_type = p_split[1]
        p_year,p_month, p_day = map(int,p_date.split("."))
        
        p_today = p_year*28*12 + p_month*28 + p_day
        print(today - (p_today + terms_dict[p_type]))
        if today >= (p_today + terms_dict[p_type]):
            answer.append(i+1)
                
    return answer
