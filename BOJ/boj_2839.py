def solution():
    # n = 18
    n = int(input())

    bags = 0
    
    while True:
        # n이 5의 배수이면 몫을 더해주고 끝낸다
        if n % 5 == 0:
            bags += n // 5
            return bags
        
        # n이 5의 배수가 아니면, 3kg을 빼고 봉지를 1더한다
        n -= 3
        bags += 1
        
        # n이 5의 배수가 되지 못하고 0이하로 떨어지면 -1을 반환한다.
        if n < 0:
            return -1
            
print(solution())
