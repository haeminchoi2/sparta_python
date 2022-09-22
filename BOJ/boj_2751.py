import sys
input=sys.stdin.readline
n = int(input())
num_list = [int(input()) for _ in range(n)]

num_list.sort()
for i in num_list:
    print(i)
