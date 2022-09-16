def solution():
    # n = 1
    n = int(input())
    prime_factors = []
    
    # 1은 소수가 아니기 때문에 소인수가 아니다.
    # n = 1일때, 아무것도 안하기 위해 2부터 시작한다.
    i = 2
    
    # 입력값 n이 소인수 i보다 클 때 반복한다.
    while n >= i:
        if n % i == 0: # i 가 소인수라면 나머지 값이 0이 된다.
            n /= i # n 을 소인수로 나눠주고 다시 선언해준다.
            prime_factors.append(i)
        elif n % i != 0:
            i += 1
    
    for factor in prime_factors:
        print(factor)
    
solution()