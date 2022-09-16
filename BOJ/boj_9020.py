# 에라토스테네스의 체
def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

t = int(input())

for _ in range(t):
    num = int(input())
    
    # num은 짝수이므로 2로 나눠서 a, b에 담아준다
    a, b = num // 2, num // 2
    
    while a > 0: # a가 0보다 클때
        # a, b 둘 다 소수라면 결과를 띄워주고 while문을 빠져나간다.
        if isPrime(a) and isPrime(b):
            print(a, b)
            break
        else: # a, b가 소수가 아닐 때 각각 -1, +1을 통해 소수인지 확인해준다.
            a -= 1
            b += 1