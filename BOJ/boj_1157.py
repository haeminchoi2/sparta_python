def solve():
    user = input()
    # user = "baaa"
    lower_user = user.lower()
    alphabets = list(set(user.lower()))
    cnt_dict = {}
    for alphabet in alphabets:
        count = lower_user.count(alphabet)
        cnt_dict[alphabet] = count
        
    sorted_dict = sorted(cnt_dict.items(), key = lambda x:x[1], reverse=1)
    if len(sorted_dict) == 1:
        result = user.upper()
        
    elif sorted_dict[0][1] == sorted_dict[1][1]:
        result = "?"
    else:
        result = sorted_dict[0][0].upper()
    
    return print(result)

solve()