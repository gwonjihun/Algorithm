from itertools import permutations

def solution(n, k):

    arr = []
    for i in range(n):
        arr.append(i+1)
        
    lists = list(permutations(arr,n))
    print(lists)
    answer = list(lists[k-1])
    return answer

print(solution(20,900))