lists = list(map(int, input().split()))
result = 0

num = 0

if len(set(lists)) == 1: # 3개가 모두 같을 때
    result = 10000 + lists[0] * 1000

elif len(set(lists)) == 3: # 모두 다를 때
    result = max(lists) * 100 # 문제에서 가장 큰 수를 100곱해서 준다했었음
    #[3, 3, 6] => 6
    #[1, 2, 2] => 2

else: # [3, 3, 6]
    for i in range(len(lists)): # 요소의 인덱스 값을 반복해본다
        if lists.count(lists[i]) == 2: # lists를 인덱싱으로 요소를 가져오고, 2개가 있는지 비교해본다
            num = lists[i] # 임의의 변수 num에 2개인 요소를 담아준다
            result = 1000 + (num * 100)

print(result)