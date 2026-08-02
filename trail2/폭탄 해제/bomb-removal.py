
# Please write your code here.

class Line:
    def __init__(self,code,color,second):
        self.code = code
        self.color = color
        self.second = second


code, color,second = list(input().split())

a = Line(code,color,second)

print(f"code : {a.code}")
print(f"color : {a.color}")
print(f"second : {a.second}")

