n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
sorted_nums = sorted(nums)

sum = 0

max = -1
for i in range(len(sorted_nums)):
    
    sum = sorted_nums[i] + sorted_nums[len(sorted_nums)-i-1]
    if sum > max:
        max = sum

print(max)