def solution():
    t = int(input())
    results = []
    for _ in range(t):
        # h = 6
        # w = 12
        # n = 10
        h, w, n = map(int, input().split())
        # floor = 1
        # num = 1
        
        num = n // h + 1
        floor = n % h
        if n % h == 0:
            num = n // h
            floor = h
        results.append(f"{floor * 100 + num}")
    for result in results:
        print(result)
solution()