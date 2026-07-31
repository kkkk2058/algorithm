

class dict:
    def __init__(self,id="codetree",level= 10):
        self.id = id
        self.level = level

id, level = list(input().split())

a = dict(id,level)

a_basic = dict()
print(f"user {a_basic.id} lv {a_basic.level}")
print(f"user {a.id} lv {a.level}")
