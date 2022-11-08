def solution(food):
    answer= []
    for i in range(1,len(food)):
        for j in range(0,food[i]//2):
            answer.append(f"{i}")
            print(i)

    answer = answer + ["0"] + answer[::-1]
    result = ''.join(answer)
    return result

print(solution([1,3,4,6]))