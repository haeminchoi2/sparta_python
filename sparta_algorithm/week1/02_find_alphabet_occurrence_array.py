def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha(): # isalpha메써드는 알파벳인지 아닌지 True, False로 반환해준다.
            continue
        arr_index = ord(char) - ord("a") # ord함수는 문자열을 ascii코드로 변환해준다.
        alphabet_occurrence_array[arr_index] += 1

    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))