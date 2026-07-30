class zero7:
    def __init__(self,code,locate,time):
        self.code = code
        self.locate = locate
        self.time = time


code , locate, time = list(input().split())
a = zero7(code,locate,time)


print(f"secret code : {a.code}")
print(f"meeting point : {a.locate}")
print(f"time : {a.time}")