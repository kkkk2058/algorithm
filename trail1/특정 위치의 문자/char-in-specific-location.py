words = ['L','E','B','R','O','S']

n = input()
idx = -1

for i, word in enumerate(words):
    if n == word:
        idx = i
        

if idx == -1:
    print('None')
else:
    print(idx)

