# numbers= []

# N = int(input())

# for _ in range(N):
#     i = int(input())
#     numbers.append(i)

# for k in range(N):
#     for m in range(N-1):
#         if numbers[m+1] < numbers[m]:
#             numbers[m] , numbers[m+1] = numbers[m+1] , numbers[m]


# for _ in range(len(numbers)):
#     print(numbers[_])


N = int(input())  # 수의 개수 입력
numbers = [int(input()) for _ in range(N)]  # 수 입력을 리스트에 저장

numbers.sort()  # 오름차순 정렬

# 정렬된 리스트를 한 줄씩 출력
for num in numbers:
    print(num)
