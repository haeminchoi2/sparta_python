from b2 import prac_module as p

num1 = int(input("숫자1을 입력해주세요. : "))
operator = input("연산자를 입력해주세요. : ")
num2 = int(input("숫자2를 입력해주세요. : "))

if operator == "+":
    result = p.plus(num1, num2)
    print(f"= {result}")
    
elif operator == "-":
    result = p.minus(num1, num2)
    print(f"= {result}")

elif operator == "*":
    result = p.times(num1, num2)
    print(f"= {result}")
    
elif operator == "/":
    result = p.div(num1, num2)
    print(f"= {result}")

else:
    print("연산할 수 없습니다.")