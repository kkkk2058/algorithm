class Product:
    def __init__(self, name, code):
        self.name = name
        self.code = code

# 1. 첫 번째 객체: 'codetree', 50으로 초기화
p1 = Product("codetree", 50)

# 2. 두 번째 객체: 사용자로부터 입력받아 생성
input_data = input().split()
p2 = Product(input_data[0], int(input_data[1]))

# 3. 출력 형식에 맞게 결과 출력
print(f"product {p1.code} is {p1.name}")
print(f"product {p2.code} is {p2.name}")