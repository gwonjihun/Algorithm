import sys
Max =1000001
DP= [0]*Max
s= [0]*Max
# DP : 인데스 값의 약수들의 합
# S : 인덱스 값보다 작은 수들의 약수들의 합에 대한 전체 SUM이기때문에
# S[i]는 S[i-1]+dp[i]를 더해주면 결과가 나온다
for i in range(1,Max):
    j = 1
    while i*j<=Max-1:
        DP[i*j]+= i
        # 위에 부분에서 i*j 2*3인경우
        # i*j의 역활 : i의 배수중 MAX보다 작은 인덱스들을 찾아주기 위해서 J와 곱을 통해서 위치 찾아줌
        j+=1
    s[i] = s[i-1]+DP[i]

t = int(input()) #테스트 케이스 개수 입력

for _ in range(t):
    a = int(sys.stdin.readline())
    sys.stdout.write(str(s[a])+"\n")

## 해당 코드는 PYPY로 동작시켜서 시간초과