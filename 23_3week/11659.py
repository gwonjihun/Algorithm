import sys
input = sys.stdin.readline
# 이게 진행되야하는 이유 : 만약에 배열의 길이가 100,000이면 입력부터 타임 아웃
N,M = map(int,input().split())

arr = list(map(int,input().split()))
sum = 0
sum_l = [0]
for i in range(N):
    sum += arr[i]
    sum_l.append(sum)
for _ in range(M):
    s,e = map(int,input().split())
    print(sum_l[e]-sum_l[s-1])