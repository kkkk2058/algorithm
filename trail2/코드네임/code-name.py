class Human:
    def __init__(self,name,score):
        self.name =name
        self.score = int(score)



humans = []

for i in range(5):
    name , score = list(input().split())
    humans.append(Human(name,score))

humans_sort = sorted(humans, key=lambda x: x.score)

# print(name,score)
a = humans_sort[0]

print(a.name, a.score)

