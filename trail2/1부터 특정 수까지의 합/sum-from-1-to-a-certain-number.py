n = int(input())

# Please write your code here.

def main(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    sum //=10
    print(sum)
    return sum

main(n)
