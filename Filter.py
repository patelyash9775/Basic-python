list1 = [1,2,3,4,5,6,7,8,9]


#filter( ) function is used to filter out the values in a list. Note that filter() function returns the result in a new list.
l1=list(filter(lambda x:x<5,list1))
print(l1)

l2=list(map(lambda x:x<5, list1))
print(l2)

l3=list(filter(lambda x:x%4==0,list1))
print(l3)