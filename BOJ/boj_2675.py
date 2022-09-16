import sys

t = int(sys.stdin.readline().rstrip())
p_list = [list(sys.stdin.readline().rstrip().split()) for i in range(t)]

result = []

for p in p_list:
    r = p[0]
    s = p[1]
    make_string = []
    for st in s:
        make_string.append(st*int(r))
    print(''.join(make_string))
