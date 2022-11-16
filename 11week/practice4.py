n, m, k = map(int,input().split())

arr = list(map(int,input().split()))
result = 0
arr.sort(reverse=1)
result = (arr[0]*k+arr[1]*1)*(m//(k+1)) + arr[0]*(m%(k+1))

print(result)
# 1 중복사용이 가능하다
# 2 그리드 문제이다.
# 3. 그러면 ? 최대 중복 개수만큼 곱해주고
# 4. 다음 인덱스 값을 곱해주는데 이때 
# 5. 다음 인덱스 값이 동일하면 if arr[0]==arr[1]일때
# result -> arr[o]*m으로 결과 도출
# 6. 아닐때 arr[0]*k + arr[1]*1 + arr[0]*k ..이런식으로
# 진행해주는데? 그 값을 구하는 방법은?
# 1 k+1 m을 나눠주면 3,1 9로 하면되는거자나