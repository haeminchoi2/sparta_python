def solution():
    # m = 3
    # n = 16

    m, n = map(int, input().split())
    
    # m부터 n까지의 숫자들을 하나씩 반복
    for prime in range(m, n+1):
        # 만약 숫자가 1이면 건너뛴다.
        if prime == 1:
            continue
        for i in range(2, int(prime**0.5)+1): # 에라토스테네스의 체
            if prime % i == 0:
                break
        else:
            print(prime)
    
    
solution()