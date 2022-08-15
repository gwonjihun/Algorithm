def solution(board, moves):
    stack = []
    answer = 0
    length = len(board)-1
    for i in moves:
        iis = i -1
        for j in range(length):
            print(f'iis : {iis}, board[{j}][{iis}] : {board[j][iis]} , stack : {stack}')
            print(board[0])
            print(board[1])
            print(board[2])
            print(board[3])
            print(board[4])
            if board[j][iis] != 0:
                if stack:
                   print(f"{i}stack[-1]:{stack[-1]},board[i][j] : {board[j][iis]}")
                else:
                   print(f'board[i][j] : {board[j][iis]}')
                if stack and stack[-1] == board[j][iis]:
                #    print(stack)
                    stack.pop()
                    answer += 2
                    board[j][iis]=0
                    break
                stack.append(board[j][iis])
                print('----------stack----------')
                print(board[0])
                print(board[1])
                print(board[2])
                print(board[3])
                print(board[4])
                #print(stack)
                board[j][iis]=0
                break

                #해당 값 스택에 던져주기 
    return answer
print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]	))
# # for i in range(4,-1,-1):
# #     print(i)