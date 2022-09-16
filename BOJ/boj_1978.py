def solution():
    # n = 4
    # numbers = [1, 3, 5, 7]
    n = int(input())
    numbers = list(map(int, input().split()))

    cnt = 0
    for number in numbers:
        # number마다 초기화 해줘야 하므로 for문 안쪽에 선언
        not_prime = 0
        if number > 1:
            # 소수는 1을 제외하므로, 범위는 2부터 자기자신까지
            for i in range(2, number):
                if number % i == 0: # 몫이 0인 i라면 not_prime 1추가
                    not_prime += 1
            # not_prime이 변화가 없으면 소수이다.
            if not_prime == 0:
                cnt += 1
    return cnt

print(solution())