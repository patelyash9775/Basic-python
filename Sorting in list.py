names = ['Earth','Air','Fire','Water']

names.sort()
print(names)

names.sort(reverse=True)
print(names)

names.sort(key=len)
print(names)

names.sort(key=len,reverse=True)
print(names)

names.pop()
print(names)