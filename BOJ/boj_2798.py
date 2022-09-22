# n = 5
# m = 21
n, m = map(int, input().split())
# numbers = [5, 6, 7, 8, 9]
numbers = list(map(int, input().split()))

def solution(n, m, numbers):
    result = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                ans_num = numbers[i] + numbers[j] + numbers[k]
                if result < ans_num <= m:
                    result = ans_num
    return result

print(solution(n, m, numbers))