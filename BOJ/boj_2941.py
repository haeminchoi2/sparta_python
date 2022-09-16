def solve():
    word = input()
    # word = "dz=ak"
    # len_word = len(word)
    croa = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
    for alpha in croa:
        if alpha in word:
            # len_word -= 1
            word = word.replace(alpha, str(croa.index(alpha)))
            # print(word)
    # print(word.index())
    result = len(word)
    return print(result)

solve()
