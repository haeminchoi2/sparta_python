from pprint import pprint

class Calc():
    # num1, num2 설정하는 메써드
    def set_number(self, num1, num2):
        try:
            self.num1 = int(num1)
            self.num2 = int(num2)
            return print(f"num1 = {self.num1}, num2 = {self.num2}")
        except ValueError:
            return print("숫자만 입력 가능합니다.")
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
        try:
            result = self.num1 / self.num2
            return f"{self.num1} / {self.num2} = {result:.2f}"
        except ZeroDivisionError:
            return "0으로 나눌 수 없습니다."

calc = Calc()
calc.set_number(20, 10)
print(calc.plus()) # 더한 값
print(calc.minus()) # 뺀 값
print(calc.multiple()) # 곱한 값
print(calc.divide()) # 나눈 값




people = [
    ("Blake Howell", "Jamaica", 18, "aw@jul.bw"),
    ("Peter Bowen", "Burundi", 30, "vinaf@rilkov.il"),
    ("Winnie Hall", "Palestinian Territories", 22, "moci@pacivhe.net"),
    ("Alfred Schwartz", "Syria", 29, "ic@tolseuc.pr"),
    ("Carrie Palmer", "Mauritius", 28, "fenlofi@tor.aq"),
    ("Rose Tyler", "Martinique", 17, "as@forebjab.et"),
    ("Katharine Little", "Anguilla", 29, "am@kifez.et"),
    ("Brent Peterson", "Svalbard & Jan Mayen", 22, "le@wekciga.lr"),
    ("Lydia Thornton", "Puerto Rico", 19, "lefvoru@itbewuk.at"),
    ("Richard Newton", "Pitcairn Islands", 17, "da@lasowiwa.su"),
    ("Eric Townsend", "Svalbard & Jan Mayen", 22, "jijer@cipzo.gp"),
    ("Trevor Hines", "Dominican Republic", 15, "ev@hivew.tm"),
    ("Inez Little", "Namibia", 26, "meewi@mirha.ye"),
    ("Lloyd Aguilar", "Swaziland", 16, "oza@emneme.bb"),
    ("Erik Lane", "Turkey", 30, "efumazza@va.hn"),
]

# filter 사용
"""
people = list(filter(lambda x: x[2] >= 20, people))
people.sort(key = lambda x: x[2])
"""

# 축약식 사용
"""
people = [x for x in people if x[2] >= 20]
people.sort(key = lambda x: x[2])
"""

# pprint(people)
