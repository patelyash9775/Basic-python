String0 = 'Taj Mahal is beautiful'

#if not find then returns -1
print (String0.index('Taj'))
print (String0.index('Mahal',0))
print()

print (String0.endswith('l',0))
print (String0.endswith('M',0,5))

print()
a = list(String0)
print (a)

print()

b = ''.join(a)
print (b,"\n")

c = '/'.join(a)[18:]
print (c,"\n")

d = c.split('/')
print (d)

