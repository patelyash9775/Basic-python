String0 = 'Taj Mahal is beautiful'
String1 = "Taj Mahal is beautiful"
String2 = '''Taj Mahal
is
beautiful'''

print (String0 , type(String0))
print (String1, type(String1))
print (String2, type(String2))


print (String0[4])
print (String0[4:])
print(String0[::-1])

print (String0.find('al'))
print (String0.find('am')) #if it is not find then returns -1

#One can also input find( ) function between which index values it has to search.
print (String0.find('j',1))
print (String0.find('j',1,3))

print (String0.capitalize())

print(String0.center(70,'-'))
print(String0.zfill(30))