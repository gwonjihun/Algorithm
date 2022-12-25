def solution(arr1, arr2):
    y_length = len(arr1)
    x_length = len(arr2[0])
    # print(x_length,y_length)
    answer = [[0 for _ in range(x_length)] for _ in range(y_length)]
    # print(answer)
    for i in range(y_length):
        for j in range(x_length):
            answer[i][j] = sum([arr1[i][k]*arr2[k][j] for k in range(len(arr1[0]))])
    return answer
    