# N = int(input())

# gx = 0
# for i in range(1,N+1):
#     fx = 0
#     for j in range(1,i+1):
#         if i%j == 0:
#             fx += j
#     gx += fx
 
# print(gx)
#### 위 코드는 시간 복잡도가 O(N)초과하기 때문에 시간 초과가 진행

N = int(input())

gx=0
for i in range(1,N+1):
    gx += (N//i)*i

print(gx)