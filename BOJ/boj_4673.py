def d():
    num_list = [i for i in range(1, 10001)]
    create_list = []
    for num in num_list:
        for n in str(num):
            num += int(n)
        create_list.append(num)
    set(create_list)
    for c_num in create_list:
        if c_num in num_list:
            num_list.remove(c_num)
    
    for result in num_list:
        print(result)
        
#     num = 1
#     while num <= 100:
#         # 생성자를 c에 저장
#         c = num
#         # 자리수를 꺼내오기 위한 for
#         for n in str(num):
#             # 자리수를 더해준다
#             c += int(n)
#         # 셀프넘버가 아닌 숫자를 리스트에서 지워준다
#         num_list.remove(c)
#         # num을 1씩 더해준다
#         num += 1
#         if num >= 100:
#             break
#     print(num_list)
d()

