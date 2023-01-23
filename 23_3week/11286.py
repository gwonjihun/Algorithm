
import heapq

n = int(input())
arr = []
answer = []
for _ in range(n):
    a = int(input())
    if a:
        # 절대값 그후 a값을 기준으로 우선순위가 정해진다.
        heapq.heappush(arr,[abs(a),a])
    else:
        # 정답을 한번에 출력하기 위해 하나의 배열에 저장한다.
        if len(arr):
            answer.append(heapq.heappop(arr)[1])
        else:
            answer.append(0)
for i in answer:
    print(i)
