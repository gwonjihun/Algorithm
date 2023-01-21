# n = int(input())
# arr = []
# for i in range(n):
#     arr.append(int(input()))

# for i in range(n):
#     changed = False

#     for j in range(n-1):
#         if arr[j]> arr[j+1]:
#             changed = True
#             arr[j], arr[j+1] = arr[j+1], arr[j]

        
#     if not changed:
#         print(i+1)
#         break
#  위는 버블소트의 원본코드이고 여기서 i는 버블소팅 과정이 몇번이 이루어졌는지를
#  찾아 출력해주는 문제이다.
#  해당 방식으로 직접 버블정렬이 동작시 시간복잡도는 O(N*N)이며 기존 데이터 범위는 500,000개이므로
#  최종적으로 시간초과가 발생하는 문제가 생긴다.

#  문제를 해결하기 위해서는 결과적으로 기존 배열에서
#  51234 -> 12345가 된다는 것은 1개의 1개가 발생하는데
#  10 1 5 2 3 -> 1 2 3 5 10이 되는 방법에서 결론적으로 1,2,3의 사이클이 돌아야지만이 버블 정렬이 끝난다
#  곧 배열 전체를 한번에 소팅하고 기존 배열과 추후 배열을 비교하며 최종적으로 배열의 이동의 횟수를 카운트하여 최대 카운트를 찾아준다

n = int(input())
arr = []
for i in range(n):
    arr.append((int(input()),i))

sorted_arr = sorted(arr)
answer = 0
for i in range(n):
    answer = max(answer, sorted_arr[i][1]-i+1)

print(answer)
