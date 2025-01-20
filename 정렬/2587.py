

numbers = []

for i in range(5):
    i = int(input())
    if i % 10 == 0 and i < 100 :
        numbers.append(i)        #for문 안에다 append를 넣어야됨

# [3,4,1,5,6,1]


# for k in range(len(a)):
average = sum(numbers) / len(numbers)


print(int(average))

median = numbers.sort() #sort 괄호까지 잘 써줘야돼

if len(numbers) % 2 == 1:       #무조건 5일때말고 홀짝일때 나눠야됨
    s = len(numbers) // 2
    print(numbers[s] )

else:
    s = len(numbers) // 2
    print((numbers[s] + numbers[s+1]) / 2)


# 제출양식을 잘 보자 