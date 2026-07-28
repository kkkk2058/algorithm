n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.

sorted_A = sorted(A)

sorted_B = sorted(B)

if sorted_A == sorted_B:
    print("Yes")
else:
    print("No")