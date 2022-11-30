from itertools import combinations
# 완전 탐색을 해주는 방법으로 가능하고
# 그리디로 해결하는 방식은?
# 음...
n = int(input())

k = int(input())
sensor = [0]*k
arr = list(map(int,input().split()))
arr.sort() 
total = 0
for i in list(combinations(range(max(arr)),k)):
    print(i)
    for k in i:
        print(k)
    # k수집국 위치 리스트
    # k수집국 위치 값을 기준으로 arr들의 값과 비교를 한다?
    # 근데 그것은 
    
    temp = []
    for j in arr:
        print(1)
# 최대와 최소의 차 /2가 수신 길이가 되는거고 
# k개의 배열을 만들어주면되는건데
# 최대한 많은 배열을 커버해주는 것도 좋지만?
# k의 위치는 찾았어 그러면 이제 k의 거리를 설정해주고
# 이게 ok이다 그러면 klist값을 
# 그러면 먼저 배열의 중앙 값을 잡아서 최대 거리를 구한다
#  결국 배열을 k개로 나누어 줘야한다.2개인데 음
# 
# k_1이 4에 있고 길이가 3이면
# 1 2 3 4 5 6 7
# k_2이 8에 있고 길이가 1이면
# 7 8 9 
# 결과는 출력이 4가 되어줘야한다.

# 720이 맞는경우
# k_1이 5에 있고 길이가 5이면
# 1 2 3 4 5 6 7 8 9
# k_2이 720에 있고 길이가 0이면
# 720