myDict={ "C":"Easy","C++":"Moderate","Java":"Tough"}

print(myDict)
print("myDict[Java]=",myDict["Java"])

myDict["PHP"]="Web"

#After adding PHP :-
print(myDict)

del myDict["C"]

#After removiing C :-
print(myDict)

print("myDict[C++]=",myDict.get("C++"))

myDict.pop("C++")

print(myDict)

myDict.clear()

#After clearing all elements :-
print(myDict)

