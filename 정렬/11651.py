# N = int(input())

# z = []

# for i in range(N):
#     n, k = map(int, input().split())
#     z.append((n, k))

# for i in range(len(z)):
#     for j in range(len(z)-1):
#         if z[j][0] > z[j+1][0] or (z[j+1][0] == z[j][0] and z[1][j+1] > z[1][j]):
#             z[j] ,z[j+1] = z[j+1] , z[j]


# for _ in range(len(z)):
#     print(z[_][0], z[_][-1])


N = int(input())

z = []

for i in range(N):
    n, k = map(int, input().split())
    z.append((n, k))

# Python의 기본 sort()를 사용하면 Timsort로 O(N log N) 시간 복잡도로 정렬할 수 있습니다.
z.sort(key = lambda x :( x[1], x[0]))

# 정렬된 결과 출력
for i in range(len(z)):
    print(z[i][0], z[i][1])
