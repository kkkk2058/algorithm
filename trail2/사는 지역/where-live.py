n = int(input())
name = []
street_address = []
region = []

for _ in range(n):
    n_i, s_i, r_i = input().split()
    name.append(n_i)
    street_address.append(s_i)
    region.append(r_i)

# Please write your code here.

class Person:
    def __init__(self, name, street_address, region):
        self.name = name
        self.street_address = street_address
        self.region = region

people = []

# 2. 이미 만들어진 3개의 리스트에서 같은 위치(인덱스)의 값들을 꺼내어 객체 생성
for i in range(n):
    obj = Person(name[i], street_address[i], region[i])
    people.append(obj)

last_person = max(people, key=lambda p: p.name)

# 4. 결과 출력
print(f"name {last_person.name}")
print(f"addr {last_person.street_address}")
print(f"city {last_person.region}")