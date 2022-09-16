def solve():
    # a = '734'
    # b = '893'
    
    a, b = input().split()
    
    sang_a = a[::-1]
    sang_b = b[::-1]
    
    if int(sang_a) > int(sang_b):
        result = sang_a
    else:
        result = sang_b
    return print(result)

solve()