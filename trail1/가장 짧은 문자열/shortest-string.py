a = input()
b = input()
c = input()

max = 0
min = 0


if len(a) >= len(b) and len(a) >= len(c):
    max = len(a)
elif len(c) >= len(b) and len(a) <= len(c):
    max = len(c)
else:
    max = len(b)


if len(a) <= len(b) and len(a) <= len(c):
    min = len(a)
elif len(a) >= len(b) and len(c) >= len(b):
    min = len(b)
else:
    min = len(c)


print(max-min)