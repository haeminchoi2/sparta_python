import random
from datetime import datetime
import time

a = int(input("몇자리 수 입니까?"))

# 랜덤한 수를 리스트형으로 생성
answer_set = set() # set 자료형으로 받아서 중복값을 없애줌
while len(answer_set) < a: # answer_set이 a자리의 숫자가 될때까지 숫자를 넣어주게 반복
    answer_set.add(random.randint(1, 9))
answer_list = list(answer_set) # 숫자의 위치가 필요하므로 list로 변형
random.shuffle(answer_list) # 랜덤하게 list의 원소를 섞어준다

# 초기값
innings = 0
start_time = time.time()

while True: # 정답을 맞출때 까지 계속 반복한다
    user_input = input(f"{a}자릿수 숫자를 입력해주세요. : ")
    if user_input == "exit": # 유저가 exit를 입력했을 때 종료한다.
        print("종료하셨습니다.")
        break
    else: # 그렇지 않으면 입력한 숫자를 리스트에 하나씩 담아준다.
        user_list = list(map(int, user_input))
    
    # 게임 내의 초기값. strike, ball은 매 회 초기화되어야 하므로 반복문 안에 위치한다.
    strike = 0
    ball = 0
    innings += 1 # 반복문이 실행될 때마다 이닝을 1씩 더해준다.
    
    # 유저가 입력한 값을 위치와 숫자까지 맞춰야 하므로 enumerate를 사용해 줌
    for i, u_num in enumerate(user_list):
        if u_num in answer_list: # 꺼내온 숫자 하나가 정답안에 있으면
            if i == answer_list.index(u_num): # 꺼내온 숫자와 정답인 숫자인덱스를 비교하여 strike 여부를 판단
                strike += 1
            else: # 꺼내온 숫자가 정답안에 있기만 하면 ball을 +1 해준다
                ball += 1
    
    # 정답일때
    if strike == a:
        end_time = time.time() # 종료되는 시점을 담아준다
        total_time = end_time - start_time # 소요시간을 담아준다.
        end_date = datetime.strftime(datetime.now(), "%y/%m/%d %H:%M")
        print(f"{innings} 번 만에 맞추셨어요!")
        print(f"{end_time-start_time:.2f}초 걸리셨습니다!")
        print(f"{end_date}")
        break
    
    # 입력한 숫자가 조건에 다 맞지않아 OUT일 때
    elif strike == 0 and ball == 0:
        print(f"{innings}회 아웃!")
        continue
    
    # 입력한 숫자가 정답은 아니고 조건에 맞는 결과를 보여준다
    else:
        print(f"{innings}회 {strike}S {ball}B")
        continue

