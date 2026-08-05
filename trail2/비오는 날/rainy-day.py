# n = int(input())


# day, week , weather = input().split()


# class data:
#     def __init__():
#         self.day = day
#         self.week = week


import sys

def solve():
    # 입력 데이터를 한 번에 읽어옵니다.
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    
    # 첫 번째 줄에서 n을 가져옵니다.
    n = int(input_data[0].strip())
    
    rainy_days = []
    
    # 두 번째 줄부터 n개의 데이터를 처리합니다.
    for i in range(1, n + 1):
        if i >= len(input_data):
            break
        line = input_data[i].strip()
        if not line:
            continue
        
        # 공백을 기준으로 날짜, 요일, 날씨를 분리합니다.
        date, day, weather = line.split()
        
        # 날씨가 'Rain'인 데이터만 리스트에 추가합니다.
        if weather == 'Rain':
            rainy_days.append((date, day, weather))
            
    # 비가 오는 날 중 날짜(yyyy-mm-dd)를 기준으로 가장 빠른(가장 근시일내) 데이터를 찾습니다.
    # 문자열 형태의 'yyyy-mm-dd'는 사전순 정렬을 통해 날짜순으로 올바르게 정렬됩니다.
    rainy_days.sort(key=lambda x: x[0])
    
    # 가장 첫 번째 데이터를 형식에 맞춰 출력합니다.
    closest_day = rainy_days[0]
    print(f"{closest_day[0]} {closest_day[1]} {closest_day[2]}")

if __name__ == '__main__':
    solve()
