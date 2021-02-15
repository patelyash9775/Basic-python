z = lambda x: x * x
z(8)

list1 = [1,2,3,4,5,6,7,8,9]

#map( ) function basically executes the function that is defined to each of the list's element separately.
eg = map(lambda x:x+2, list1)
print (list(eg))

list2 = [9,8,7,6,5,4,3,2,1]
eg2 = list(map(lambda x,y:x+y, list1,list2))
print(eg2)

eg3 = map(str,eg2)
eg3=list(eg3)
print(eg3)