################# 내 풀이
# def solve():
#     user = input()
#     # user = "baaa"
#     lower_user = user.lower()
#     alphabets = list(set(user.lower()))
#     cnt_dict = {}
#     for alphabet in alphabets:
#         count = lower_user.count(alphabet)
#         cnt_dict[alphabet] = count
        
#     sorted_dict = sorted(cnt_dict.items(), key = lambda x:x[1], reverse=1)
#     if len(sorted_dict) == 1:
#         result = user.upper()
        
#     elif sorted_dict[0][1] == sorted_dict[1][1]:
#         result = "?"
#     else:
#         result = sorted_dict[0][0].upper()
    
#     return print(result)

# solve()

################### 권기현 튜터님 풀이
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

word = input().upper()

max_alpahbet = ""
max_count = 0

for alphabet in alphabets:
    n = word.count(alphabet) # 알파벳중 하나가 word입력값 안에 몇개나 있는지
    if n > max_count: # word안에 알파벳 하나가 max_count보다 클 때
        max_count = n # n이 max_count가 된다.
        max_alpahbet = alphabet # max_count가 된 알파벳을 max_alphabet이 된다.
    elif n == max_count: # 많이 사용된 알파벳이 여러 개 존재하는 경우
        max_alpahbet = "?"
    else:
        continue
    
print(max_alpahbet)