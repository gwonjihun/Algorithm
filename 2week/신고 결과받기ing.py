# setss = {'a':[1,2,3],'b':[1,2,3,1]}
# # 먼저 dict로 초기에 신청한 값들을 넣어준다
# # 그뒤에 dict의 value들을 set으로 전환시켜서 중복 제거
# # 그리고 dict로 선언된 id_list를 새로 만들어서 거기서 해당하는 이름에 +1을 해준다
# # 그리고 해당 items값이 2이상이되면 answer인 k값을 1 증가시킨다
# print(setss)
# print(temp)

def solution(id_list, report, k):
    dicts = {}
    
    answer = []
    return answer