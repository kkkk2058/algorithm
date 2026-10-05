n = int(input())
name = []
korean = []
english = []
math = []

student = []
for _ in range(n):
    student_info = input().split()
    name.append(student_info[0])
    korean.append(int(student_info[1]))
    english.append(int(student_info[2]))
    math.append(int(student_info[3]))
student=list(zip(name,korean,english,math))
# Please write your code here.
#udent.sort(key = lambda x: (-x[1][0],-x[2][0],-x[3][0]))
student.sort(key=lambda x: (-x[1], -x[2], -x[3]))


for name, korean, english, math in student:
    print(name, korean, english, math)

