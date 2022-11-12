def solution(reference,track):
    short_len = 1e9
    idx = 0 
    while idx < len(track):
        tmp_len = 0
        for i in range(0,len(reference)):
            if 0 <= idx < len(track):
                if track[idx]== reference[i]:
                    tmp_len+=1
                    idx += 1
        if tmp_len < short_len:
            short_len = tmp_len

    return short_len

print(solution("abcde",'abceabcdeabcdabcaba'))