names = ['One', 'Two', 'Three', 'Four', 'Five']
numbers = [1, 2, 3, 4, 5]

d2 = zip(names,numbers)
print (list(d2))

a1={}
for i in range(len(names)):
    a1[names[i]] = numbers[i]
print (a1)

#Only the value is stored and not the key in pop function
a2 = a1.pop('Four')
print (a1)
print (a2)