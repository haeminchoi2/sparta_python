input = [3, 5, 6, 1, 2, 4]

################ 내 풀이
# def find_max_num(array):
#     return max(array)

# result = find_max_num(input)
# print(result)

################ 강의 풀이
def find_max_num(array):
    for num in array:
        for compare_num in array:
            if num < compare_num:
                break
        # for else문
        # for문이 다 끝날때까지 한번도 break되지 않으면 실행된다.
        else:
            return num


result = find_max_num(input)
print(result)