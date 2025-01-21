# N = int(input())

# k= []
# k = set()


# for _ in range(N):
#     a = str(input())
#     k.add(a)

# k = list(k)

# for i in range(len(k)):
#     for j in range(len(k)-1):
#         if len(k[j]) > len(k[j+1]):
#             k[j] ,k[j+1] =  k[j+1] ,k[j]


# for i in range(len(k)):
#     for j in range(len(k)-1):
#         if k[j] > k[j+1]:
#             k[j] ,k[j+1] =  k[j+1] ,k[j]

# for _ in k:
#     print(_)

        

N = int(input())

k= []
k = set()


for _ in range(N):
    a = str(input())
    k.add(a)

k = sorted(k, key= lambda x: (len(x), x))

# k.sort 하려했는데 set은 sort할 수 없어 이렇게 k = sorted이렇게 따로 해줘야됨

for word in k:
    print(word)