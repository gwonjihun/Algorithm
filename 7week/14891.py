from collections import deque

def split_arr(s):
    result = deque([ int(i) for i in s])
    return result

# 2과 6 위치 값을 기준으로
# 비교해서 회전 유무 판단이 먼저
#

arr =  {i:split_arr(input())for i in range(0,4)}

case = int(input())

def check_left(start,dirs):
    if start<0 or arr[start][2]==arr[start+1][6]:
        return
    if arr[start][2]!=arr[start+1][6]:
        check_left(start-1,-dirs)
        arr[start].rotate(dirs)
        # print(arr)

def check_right(start,dirs):
    if start>3 or arr[start][6]==arr[start-1][2]:
        return
    if arr[start][6]!=arr[start-1][2]:
        check_right(start+1,-dirs)
        arr[start].rotate(dirs)
        # print(arr)

for _ in range(case):
    start, dire = map(int,input().split())
    # 1234로 start는 들어온다
    # arr는 0,1,2,3만 사용 가능하다
    # 고로 start에서 3이 들어오면 배열에서는 2로 알아봐줘야한다.
    check_right(start+1-1,-dire)
    check_left(start-1-1,-dire)
    arr[start-1].rotate(dire)
    # print(arr)
# 방향을 어떻게 해줄꺼냐?
# 예를 들어 2 일때 +1
result = 0
for i in range(0,4):
    result += arr[i][0]*(2**i)
print(result)