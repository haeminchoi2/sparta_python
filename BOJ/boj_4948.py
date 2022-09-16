########################시간초과
# def solution():
#     # n = 10
    
#     cnt_list = []
#     while True:
#         n = int(input())
#         if n == 0:
#             break
        
#         cnt = 0
#         # m부터 n까지의 숫자들을 하나씩 반복
#         for prime in range(n, (2 * n) + 1):
#             # # 만약 숫자가 1이면 건너뛴다.
#             # if prime == 1:
#             #     continue
#             for i in range(2, int(prime**0.5)+1): # 에라토스테네스의 체
#                 if prime % i == 0:
#                     break
#             else:
#                 cnt += 1
#         cnt_list.append(cnt)
    
#     for c in cnt_list:
#         print(c)

###################### 답안 참고

# 에라토스테네스의 체
def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# 문제의 범위가 1 <= n <= 123,456 이기 때문에 2부터 2n까지 리스트로 만들어준다.
# [x for x in range(1 * 2, (123456 * 2) + 1)]
prime_list = [x for x in range(2, 246913)]

# 빈 리스트를 만들어 prime_list를 반복하며 소수를 추가해 줄 것이다.
results = []

for prime in prime_list:
    # 만약 소수라면 isPrime() 함수에서 True를 반환
    if isPrime(prime):
        # 결과 리스트에 prime을 추가해줌
        results.append(prime)

while True:
    cnt = 0
    num = int(input())
    
    # 0 을 입력받으면 종료
    if num == 0:
        break
    
    for result in results:
        if num < result <= 2*num:
            cnt += 1
            
    print(cnt)