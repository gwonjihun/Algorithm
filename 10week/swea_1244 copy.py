from itertools import permutations
def solution(marbles):
    result = []
    for i in range(len(marbles),0,-1):
        for j in list(permutations(marbles,i)):
            print(list(j))

print(solution([1,2,3,4,5]))