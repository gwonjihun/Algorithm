def solution(numbers):
    lists = [i for i in range(10)]
    print(lists)
    for i, n in enumerate(numbers):
        if n in numbers:
            lists[n] = 0
    answer = 0
    print(lists)
    for i, n in enumerate(lists):
        answer+=n
    
    return answer

print(solution([1,2,3,4,5,6,7]))