# 원반이 1개일때
# 1 -> 3

# 원반이 2개일때
# 1 -> 2
# 1 -> 3
# 2 -> 3
n = int(input())

def hanoi(n, start, second, target):
    if n == 1: # 제일 아래의 큰 원판을 목표 기둥에 옮긴다
        print(f"{start} {target}")
        return
    hanoi(n - 1, start, target, second) # 제일 큰 원판을 뺀 원판들을 보조 기둥에 옮긴다.
    hanoi(1, start, second, target) # 제일 큰 원판을 목표 기둥에 옮긴다
    hanoi(n - 1, second, start, target) # 보조기둥에 있는 나머지 원판들을 목표 원판으로 옮긴다.
    return

cnt = 2**n - 1
print(cnt)
hanoi(n, 1, 2, 3)
