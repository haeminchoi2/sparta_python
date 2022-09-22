n = int(input())

array_ = [int(input()) for _ in range(n)]

def sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left_array = sort(array[:mid])
    right_array = sort(array[mid:])
    return merge(left_array, right_array)

def merge(array1, array2):
    result = []
    array1_i = 0
    array2_i = 0
    while array1_i < len(array1) and array2_i < len(array2):
        if array1[array1_i] < array2[array2_i]:
            result.append(array1[array1_i])
            array1_i += 1
        else:
            result.append(array2[array2_i])
            array2_i += 1
            
    if array1_i == len(array1):
        while array2_i < len(array2):
            result.append(array2[array2_i])
            array2_i += 1
            
    if array2_i == len(array2):
        while array1_i < len(array1):
            result.append(array1[array1_i])
            array1_i += 1
            
    return result

for number in sort(array_):
    print(number)