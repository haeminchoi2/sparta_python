import sys

n = sys.stdin.readline().rstrip()

if int(n) < 10:
    n += '0' # n = 10

test = n
cnt = 1

while True:
    n2 = str(int(n[0]) + int(n[1]))
    n3 = n[-1] + n2[-1]

    if n3 == test:
        print(cnt)
        break

    else:
        cnt += 1
        n = n3
        continue

