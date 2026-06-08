# a,s,d,f,g,h,j,k,l,z = map(int,input().split())

# 원래 인자의 개수만큼 변수를 주면 그대로 받는다.
# 이걸 다 적을 수가 없잖아

num_list = list(map(int,input().split()))

# print(num_list[0])
sum = 0
avg = 0
for i in range(len(num_list)):
    if num_list[i] < 250:
        sum += num_list[i]
        if i == len(num_list)-1:
            avg = sum / (i+1)
            
    else:
        avg = sum / (i)
        break
print(f"{sum} {avg:.1f}")
