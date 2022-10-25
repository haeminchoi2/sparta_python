# n = "2143"
n = input()
numbers = [x for x in n]
numbers.sort(key=lambda x: x, reverse=True)
print(''.join(numbers))