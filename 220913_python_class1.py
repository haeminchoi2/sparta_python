from pprint import pprint

class Area():
    # 인스턴스 생성시 가로a, 세로b를 저장.
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)
        self.PIE = 3.14
        print("인스턴스 생성!")
    
    # 사각형의 넓이 구하기
    def square(self): # 클래스 안의 함수 = 메써드
        result = self.a * self.b
        return f"rec : {result}"
    
    # 삼각형의 넓이
    def triangle(self):
        result = (self.a * self.b) / 2
        return f"tri : {result:.2f}"
    
    # 원의 넓이
    def circle(self):
        result = ((self.a)/2 ** 2) * self.PIE
        return f"circle : {result:.2f}"


class Calc():
    # num1, num2 설정하는 메써드
    def set_number(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        return f"num1 = {self.num1}, num2 = {self.num2}"
        
    # 더하기 연산
    def plus(self):
        result = self.num1 + self.num2
        return f"{self.num1} + {self.num2} = {result}"
        
    # 뺄셈
    def minus(self):
        result = self.num1 - self.num2
        return f"{self.num1} - {self.num2} = {result}"
    
    # 곱셈
    def multiple(self):
        result = self.num1 * self.num2
        return f"{self.num1} * {self.num2} = {result}"

    # 나눗셈
    def divide(self):
        result = self.num1 / self.num2
        return f"{self.num1} / {self.num2} = {result:.2f}"

class Profile():
    # 빈값의 초기 프로필
    def __init__(self):
        self.profile = {
            "name": "-",
            "gender": "-",
            "birthday": "-",
            "age": "-",
            "phone": "-",
            "email": "-",
        }
    
    # profile파라미터로 초기 프로필을 바꿔서 설정해준다.
    def set_profile(self, profile):
        self.profile = profile
    
    
    def get_name(self):
        return f"name : {self.profile['name']}"
    
    def get_gender(self):
        return f"gender : {self.profile['gender']}"
    
    def get_birthday(self):
        return f"birthday : {self.profile['birthday']}"
    
    def get_age(self):
        return f"age : {self.profile['age']}"
    
    def get_phone(self):
        return f"phone : {self.profile['phone']}"
    
    def email(self):
        return f"email : {self.profile['email']}"
