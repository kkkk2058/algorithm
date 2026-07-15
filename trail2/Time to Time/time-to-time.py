a, b, c, d = map(int, input().split())


hour = 0
minute = 0

min = 0
hour = a
minute = b
while True:
    if hour == c and minute == d:
        print(min)
        break
    minute +=1
    min +=1

    if hour >=24:
        hour = 0
        minute = 0

    if minute >= 60:
        hour +=1
        minute = 0

    