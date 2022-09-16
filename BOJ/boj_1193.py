# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
def solution():
    x = int(input())
    
    # idx가 있는 n줄에 n개의 분수가 들어있다.
    n = 1
    idx = 1

    # 입력값이 1이면 1/1을 반환
    if x == 1:
        result = "1/1"
        return result

    else:
        while idx < x:
            idx += n + 1
            n += 1
        
        idx_delta = idx - x

        if n % 2 == 0: # 짝수인 n번째 칸에 있으면 분수가 1부터 증가하고, 분자는 n부터 감소한다
            result = f"{n - idx_delta}/{1 + idx_delta}"
            return result
        else:
            result = f"{1 + idx_delta}/{n - idx_delta}"
            return result

print(solution())