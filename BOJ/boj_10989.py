import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
# arr = [5, 2, 3, 1, 4, 2, 3, 5, 1, 7]

# arr의 숫자가 몇 개 존재하는지 갯수를 저장하기 위한 count
# 0 ~ 최댓값까지 인덱스를 사용할 수 있도록 최대값 + 1
# [0, 0, 0, 0, 0, 0, 0, 0]
count = [0] * (max(arr) + 1)

for number in arr:
    count[number] += 1 # count[5]는 숫자 5가 arr에 몇 개인지 알려주는 data

# count 배열의 원소를 누적합으로 갱신
for index in range(1, len(count)): # arr의 원소를 result 정렬된 index값으로 넣기위한 작업
    count[index] += count[index - 1]

result = [0] * len(arr)

for number in arr:
    index = count[number]
    result[index - 1] = number
    count[number] -= 1

for num in result:
    print(num)