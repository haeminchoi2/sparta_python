input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha(): # isalpha메써드는 알파벳인지 아닌지 True, False로 반환해준다.
            continue
        arr_index = ord(char) - ord("a") # ord함수는 문자열을 ascii코드로 변환해준다.
        alphabet_occurrence_array[arr_index] += 1

    max_occurrence = 0
    max_alphabet_index = 0
    for index in range(len(alphabet_occurrence_array)):
        # index 0 -> alphabet_occurrence 3
        alphabet_occurrence = alphabet_occurrence_array[index]
        
        if alphabet_occurrence > max_occurrence:
            max_alphabet_index = index
            max_occurrence = alphabet_occurrence
    
    return chr(max_alphabet_index + ord('a'))


result = find_max_occurred_alphabet(input)
print(result)