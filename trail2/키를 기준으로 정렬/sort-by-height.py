import sys

# 1. 사람의 수 n 입력받기
n = int(sys.stdin.readline())

# 2. n명의 정보 입력받아 리스트에 저장하기
people = []
for _ in range(n):
    name, height, weight = sys.stdin.readline().split()
    # 키와 몸무게는 숫자로 비교해야 하므로 정수(int)형으로 변환합니다.
    people.append((name, int(height), int(weight)))

# 3. 키(x[1])를 기준으로 오름차순 정렬하기
# 문제 조건에 동일한 키가 주어지지 않는다고 했으므로 키만 고려하면 됩니다.
people.sort(key=lambda x: x[1])

# 4. 정렬된 결과 출력하기
for p in people:
    print(f"{p[0]} {p[1]} {p[2]}")
