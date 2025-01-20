# numbers = []

N, k = map(int, input().split())

array = list(map(int, input().split())) # 공백을 두고 여러개의 문자를 입력받는법, list로 바로 저장하는 방법

# numbers.append(array)

# for a in range(len(array)):
#     for k in range(len(array)-1):
#         if array[]


array.sort()

print(array[N-k])

