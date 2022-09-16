import sys, string

s = sys.stdin.readline().rstrip()

alphabets = list(string.ascii_lowercase)

n = 0
while True:
    try:
        if alphabets[n] in s:
            alphabets[n] = s.index(alphabets[n])
            n += 1
        else:
            alphabets[n] = -1
            n += 1
    except:
        break

print(' '.join(map(str, alphabets)))