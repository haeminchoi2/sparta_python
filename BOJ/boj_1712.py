def solve():
    
    a, b, c = map(int, input().split())
    # a, b, c = 2100000000, 9, 10
    
    # cx=bx+a
    # cx-bx=a
    # (c-b)x=a
    # x=a/c-b
    
    if b < c:
        result = a // (c-b) +1
    else:
        result = -1
    return result
print(solve())