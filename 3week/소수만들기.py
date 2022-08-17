from itertools import combinations 
def solution(nums):
    answer = []
    menu = list(map(sum,combinations(nums,3)))
    #print(menu)
    for i in menu:
        flag =0
        for j in range(2,i):
            print(f'{i}%{j} = {i%j}')
            if i%j ==0:
                flag = 1
                break
        if flag != 1:
            answer.append(i)
    return answer

print(solution([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]))