# 1. 조건문
# def get_grade(score):
#     if 90 < score <= 100:
#         return "A"
#     elif 80 < score <= 90:
#         return "B"
#     elif 70 < score <= 80:
#         return "C"
#     else:
#         return "F"


# score = int(input())
# grade = get_grade(score)
# print(grade)

# 2. 반복문
cnt = 1
while cnt <= 5:
    user_input = input("종료하고싶으면 exit 를 입력해주세요. : ")
    if user_input == "exit":
        break
    try:
        cnt += 1
        twice = int(user_input) * 2
        print(twice)
    except ValueError:
        print(f"입력한 문자는 {user_input} 입니다.")

# 3. 반복문
# from pprint import pprint

# users = [
#     {"name": "Ronald", "age": 30, "math_score": 93, "science_score": 65, "english_score": 93, "social_score": 92},
#     {"name": "Amelia", "age": 24, "math_score": 88, "science_score": 52, "english_score": 78, "social_score": 91},
#     {"name": "Nathaniel", "age": 28, "math_score": 48, "science_score": 40, "english_score": 49, "social_score": 91},
#     {"name": "Sally", "age": 29, "math_score": 100, "science_score": 69, "english_score": 67, "social_score": 82},
#     {"name": "Alexander", "age": 30, "math_score": 69, "science_score": 52, "english_score": 98, "social_score": 44},
#     {"name": "Madge", "age": 22, "math_score": 52, "science_score": 63, "english_score": 54, "social_score": 47},
#     {"name": "Trevor", "age": 23, "math_score": 89, "science_score": 88, "english_score": 69, "social_score": 93},
#     {"name": "Andre", "age": 23, "math_score": 50, "science_score": 56, "english_score": 99, "social_score": 54},
#     {"name": "Rodney", "age": 16, "math_score": 66, "science_score": 55, "english_score": 58, "social_score": 43},
#     {"name": "Raymond", "age": 26, "math_score": 49, "science_score": 55, "english_score": 95, "social_score": 82},
#     {"name": "Scott", "age": 15, "math_score": 85, "science_score": 92, "english_score": 56, "social_score": 85},
#     {"name": "Jeanette", "age": 28, "math_score": 48, "science_score": 65, "english_score": 77, "social_score": 94},
#     {"name": "Sallie", "age": 25, "math_score": 42, "science_score": 72, "english_score": 95, "social_score": 44},
#     {"name": "Richard", "age": 21, "math_score": 71, "science_score": 95, "english_score": 61, "social_score": 59},
#     {"name": "Callie", "age": 15, "math_score": 98, "science_score": 50, "english_score": 100, "social_score": 74},
# ]
# def get_filter_user(users):
#     filter_users = []
#     for user in users:
#         sum_score = user['math_score'] + user['science_score'] + user['english_score'] + user['social_score']
#         avg_score = sum_score / 4
#         if avg_score >= 70:
#             # del user['math_score']
#             # del user['science_score']
#             # del user['english_score']
#             # del user['social_score']
#             # filter_users.append(user)
#             filter_users.append({"age" : user['age'], 
#                                  "name" : user['name']})
#     return filter_users

# filter_users = get_filter_user(users)
# pprint(filter_users)