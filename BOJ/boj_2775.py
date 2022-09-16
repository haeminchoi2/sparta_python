
# 4층 1 6 21 56 126
# 3층 1 5 15 35 70
# 2층 1 4 10 20 35
# 1층 1 3 6 10 15
# 0층 1 2 3 4 5
def solution():
    t = int(input())

    # k = 1
    # n = 3
    results = []
    for _ in range(t):
        k = int(input())
        n = int(input())

        lives_0F = [x for x in range(1, n+1)]

        for floor in range(k):
            lives_kF = []
            for i in range(len(lives_0F)):
                live = sum(lives_0F[:i+1])
                lives_kF.append(live)
            lives_0F = lives_kF

        results.append(lives_kF[n-1])

    for result in results:
        print(result)
solution()

