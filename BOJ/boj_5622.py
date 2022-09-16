def solve():
    word = input()
    # word = "WA"
    dial = {
        "2" : ["A", "B", "C"],
        "3" : ["D", "E", "F"],
        "4" : ["G", "H", "I"],
        "5" : ["J", "K", "L"],
        "6" : ["M", "N", "O"],
        "7" : ["P", "Q", "R", "S"],
        "8" : ["T", "U", "V"],
        "9" : ["W", "X", "Y", "Z"],
    }
    result = 0
    for alpha in word:
        for key in dial:
            if alpha in dial[key]:
                result += int(key) + 1
            
    return print(result)

solve()