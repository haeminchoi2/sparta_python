import sys

def solve():
    n = sys.stdin.readline().rstrip()
    n_list = []

    # 1부터 입력받은 n까지 하나씩 반복한다
    for number in range(1, int(n)+1):
    # n = "1"

        # number가 int이기때문에 자릿수를 쉽게 비교하기 위해 str로 변환
        str_num = str(number)
        
        # 자리수 마다 차이를 x_list에 저장해서 비교할것임
        x_list = []
        
        # 인덱스 값을 가져와서 차이를 구하고 x_list에 추가해준다
        for i in range(len(str_num) - 1):
            # 현재 i인 인덱스와 i+1의 인덱스를 비교하기 때문에
            # 위의 범위에서 -1을 해주어 끝자리에서 인덱스가 하나 더 넘어가는
            # 에러를 피하기 위함
            x = int(str_num[i]) - int(str_num[i + 1])
            x_list.append(x)
        
        if len(set(x_list)) == 1:
            n_list.append(number)
        elif len(set(x_list)) == 0:
            n_list.append(number)
        
    print(len(n_list))
        

solve()