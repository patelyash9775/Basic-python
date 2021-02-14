myList=["C","C++","Python"]

print(myList)

print("length of list : ",len(myList))

print("myList[1]=",myList[1])

print()
print("After appending : ",end="")
myList.append("Java")

print(myList)

print()
print("After inserting : ",end="")
myList.insert(1,"HTML")

print(myList)

print()
print("After removing : ",end="")
myList.remove("C++")

print(myList)

myList.sort()
print()
print("Sorted list : ",myList)

print()
myList.sort(reverse=True)
print("Reverse sorted list : ",myList)
