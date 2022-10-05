def split_input(ins):
    return [ int(i) for i in ins]

n , m = map(int,input().split())

arr = [split_input(input()) for _ in range(n)]
minmum = -1
print(arr)