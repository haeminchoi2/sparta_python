import math
# a = 5
# b = 1
# v = 6
def solution():
    a, b, v = map(int, input().split())

    lastday_climb = v - b

    climb_per_day = a - b

    return math.ceil(lastday_climb / climb_per_day)

print(solution())