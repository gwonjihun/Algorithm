state = input()
nums = []
temp=''

# 초기 입력값을 기호와 숫자로 분리
for i in state:
    if i.isnumeric():
        temp += i
        continue
    else:
        nums.append(temp)

        nums.append(i)
        temp = ''
        continue
# 마지막 숫자가 안들어가므로 추가
nums.append(temp)

flag = 0
# 문자열에 왼쪽 0값들 제거
for i in range(len(nums)):
    if nums[i].isnumeric():
        nums[i] = nums[i].lstrip('0')

# -를만날때 () 추가
for i in range(len(nums)):
    if nums[i]=='-' and flag==0:
        nums[i+1] = '('+ nums[i+1]
        flag =1
    elif nums[i]=='-' and flag == 1:
        nums[i+1] = '('+ nums[i+1]
        nums[i-1] = nums[i-1]+')'
        flag = 1
    if flag == 1 and i == len(nums)-1:
        nums[i] = nums[i]+')' 
        flag = 0 
print(eval(''.join(nums)))

