state = input()
nums = []
plus = []
temp=''
for i in state:
    if i.isnumeric():
        temp += i
        continue
    else:
        nums.append(temp)

        nums.append(i)
        temp = ''
        continue
nums.append(temp)

flag = 0

for i in range(len(nums)):
    if nums[i].isnumeric():
        nums[i] = nums[i].lstrip('0')

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

