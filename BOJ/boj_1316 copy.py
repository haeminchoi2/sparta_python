

def solve():
    n = int(input())
    word_list = [input() for i in range(n)]
    
    # give_word = list("happy")
    # ['h', 'a', 'p', 'p', 'y']
    # alpha_list = list(set(give_word))
    # ['h', 'p', 'a', 'y']

    cnt = 0 # 단어의 갯수를 세기 위함
    for j in word_list: # 입력 받은 word_list를 반복문으로 하나씩 꺼내온다
        give_word = list(j) # 문자열 j를 한글자씩 list
        alpha_list = list(set(give_word)) # 중복되는 알파벳을 제거하여 사용된 알파벳만 취급
        
        if len(alpha_list) == 1: # 예를 들어 단어가 한 글자일 경우 그룹단어로 취급
            cnt += 1
            
        else: # 단어가 한글자 이상일 경우
            for word in give_word: # 입력받은 문자열을 한글자씩 꺼내옴
                word_i = give_word.index(word) # 꺼내온 글자의 인덱스값을 담아줌
                if word_i == len(give_word) - 1: # 반복문이 문자열 끝까지 수행했다면, 그룹 단어가 맞음
                    cnt += 1
                else:
                    if word in alpha_list: # 꺼내온 글자가 사용된 알파벳리스트 안에 있으면
                        if word != give_word[word_i + 1]: # 꺼내온 알파벳이 다음 index값의 알파벳과 다르다면,
                                                            # 사용된 알파벳을 제거해줌
                            alpha_list.remove(word)
                        elif word == give_word[word_i + 1]:
                            pass
                    else: # 꺼내온 글자가 사용된 알파벳리스트 안에 없으면 반복문 탈출
                        break

    result = cnt
    return result
print(solve())




        # if word_i == len(give_word) - 1:
        #     cnt += 1
        
        # elif word != give_word[word_i + 1]:
        #     alpha_list.remove(word)
        
        # elif word == give_word[word_i + 1]:
        #     continue
        
        # else:
        #     break
    