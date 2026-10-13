n = int(input())

name = []
score1 = []
score2 = []
score3 = []
student = []

class Student:
    def __init__ (self, name,kor, eng, math):
        self.name = name
        self.kor = kor 
        self.eng = eng
        self.math = math

for _ in range(n):
    student_input = input().split()
    name = (student_input[0])
    kor = int(student_input[1])
    eng = int(student_input[2])
    math = int(student_input[3])

    student.append(Student(name,kor,eng,math))

# Please write your code here.


student.sort(key = lambda x : x.kor + x.eng + x.math, reverse = False)

for i in student:
    print(i.name, i.kor,i.eng,i.math)