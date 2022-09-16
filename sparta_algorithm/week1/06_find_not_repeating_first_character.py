input = "abadabac"

def find_not_repeating_character(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha(): # isalpha메써드는 알파벳인지 아닌지 True, False로 반환해준다.
            continue
        arr_index = ord(char) - ord("a") # ord함수는 문자열을 ascii코드로 변환해준다.
        alphabet_occurrence_array[arr_index] += 1
    not_repeating_character_array = []
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]
        if alphabet_occurrence == 1:
            not_repeating_character_array.append(chr(index + ord("a")))
    
    for char in string:
        if char in not_repeating_character_array:
            return char



result = find_not_repeating_character(input)
print(result)