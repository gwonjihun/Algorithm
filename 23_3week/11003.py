import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
arr = list(map(int,input().split()))
q = deque()
for i in range(n):
    # 첫번째 while문을 통해서 Ai ~ Ai-m+1의 배열 중 무조건 포함되는 Ai를 기준으로
    # Ai보다 큰 값은 목록에서 제외해준다.
    while q and q[-1][1] > arr[i]:
        q.pop()

    # 두번째 while 문을 통해서 배열의 index가 i-m+i보다 작은 인덱스를 제거해준다. 왜냐
    # 배열은 i가 m전까지는 무조건 1개만을 검색하고
    # i가 m +1 이상인 상황에서부터 배열의 범위는 2개 이상으로 증가한다.
    # 고로코롬 i-m+1보다 작다는 뜻은 범위 내부에 있는 값을 검사하게 해준다.
    while q and q[0][0] < i-m+1:
        q.popleft()
    q.append([i,arr[i]])
    print(q[0][1], end=' ')


# for i in range(1,n+1): # 1~12까지 조회
#     d = i+1-m
#     if d <=0: 
#         d = 1
#     if i> d:
#         # print("i:",i,d,arr[d:i+1])
#         ans.append(min(arr[d:i+1]))
#     elif i < d:

#         # print("d:",i,d,arr[i:d+1])
#         ans.append(min(arr[i:d+1]))
#     else:
#         # print("i==d",i,d,arr[i])
#         ans.append(arr[i])

# for i in ans:
#     print(i,end=" ")

#  위 문제의 n의 갯수는 맥스 5,000,000개인데 
#  처음에 생각했을때 for문 하나닌깐 0(n)으로 판단
#  하지만 사실 min이라는 함수로 인해서 O(3n*n)이기 떄문에 
#  for문 하나만을 사용하게 된다면 결국 타임오버
