INF = 1e9
n, m = list(map(int, input().split()))


array = [[INF]*(n+1) for i in range(n+1)]


for i in range(m):
    A, B = list(map(int, input().split()))

    array[A][B] = 1

# 자기 자신 방향은 0
for i in range(n+1):
    array[i][i] = 0

# i -> k -> j가 i -> j보다 작다면 값을 교체
# 결과 적으로 i -> j의 최소 이동비용을 선택되며
# 예를 들어 1-> 6 의 최소비용이 1 ->2 -> 4 -> 5 여도
#  1->4의 비용은 1->2->4가 저장되어 있으므로 3중첩 for문으로 해결이 가능
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            array[i][j] = min(array[i][k] + array[k][j], array[i][j])

print(*array, sep='\n')

result = 0

# 최종적으로 배열에서 행 혹은 열 중 하나를 기준으로 선택하여
# 행 또는 열에서 INF가 없으면 해당 인덱스는 순위를 알 수 있음
for i in range(1, n+1):
    count = 0
    for j in range(1, n+1):
        if array[i][j] != INF:
            count += 1
    if count == n:
        result += 1
print(result)