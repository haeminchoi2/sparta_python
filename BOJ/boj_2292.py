# 1 6 12 18 24
#  5 6  6  6
# 1 7 19 37 61
#  6 12 18 24 

def solution():
    # n = 13
    n = int(input())
    cnt = 1
    end_num = 1

    while True:
        if n == 1:
            break
        else:
            if n > end_num:
                end_num += 6 * cnt
                cnt += 1
            else:
                break
            
    result = cnt
    return result
print(solution())