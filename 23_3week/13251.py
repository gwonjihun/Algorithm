import math
c_m = int(input())
# 색상 종류
# 2번째 줄은 색상별 조약돌 갯수
# 3번째 조약돌을 뽑는 갯수

arr = list(map(int,input().split()))

k = int(input())
arr_sum = sum(arr)
pic_sum = 0
bottom = 1
# totlaCk의 경우의 수를 구함
for i in range(k):
    bottom = bottom*arr_sum
    arr_sum-=1
# 색상 별로 반복문 실행
for i in range(c_m):
    temp_total = 1
    for j in range(k):
        temp_total = temp_total * arr[i]
        arr[i]-=1
    pic_sum+= temp_total

print(pic_sum/bottom)