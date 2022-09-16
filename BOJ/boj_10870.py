# n = 10
n = int(input())

def fibo(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    array_ = [0, 1]
    while len(array_) <= num:
        number = array_[len(array_) - 1] + array_[len(array_) - 2]
        array_.append(number)
    return array_[num]

print(fibo(n))