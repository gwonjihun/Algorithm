n = input()
answer = 0
for i in n:
    answer = max(answer+int(i), answer*int(i))
print(answer)