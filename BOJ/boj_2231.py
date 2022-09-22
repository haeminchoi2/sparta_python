def solution():
    n = int(input())

    for i in range(1, n + 1): # 1부터 n까지 생성자가 맞는지 확인한다.
        num_list = [int(x) for x in str(i)] # 문자열로 바꿔 각 자리수를 리스트로 만든다
        sum_num = i + sum(num_list) # 1~n 숫자를 생성자인지 확인하기위해 더해준다
        if sum_num == n: # 생성자가 맞으면
            return i # i를 반환
    return 0 # 반복문이 끝날때까지 return 하지못했으면 0을 반환
print(solution())
