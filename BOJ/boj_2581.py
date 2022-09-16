def solution():
    m = 3
    n = 16

    # m = int(input())
    # n = int(input())

    # 소수들을 담기위한 빈 리스트 생성
    primes = []
    
    # m부터 n까지의 숫자들을 하나씩 반복
    for prime in range(m, n+1):
        # 만약 숫자가 1이면 건너뛴다.
        if prime == 1:
            continue
        not_prime = 0 # 소수가 아님을 판별하기위한 변수
        for i in range(2, prime):
            if prime % i == 0:
                not_prime += 1
        if not_prime == 0:
            primes.append(prime)
    
    for number in primes:
        print(number)
    
solution()