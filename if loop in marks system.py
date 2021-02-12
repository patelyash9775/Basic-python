marks=float(input("Enter your marks : "))

print("Grade : ",end="")

if marks>=90:
    print("O")
elif marks>=80:
    print("+A")
elif marks>=70:
    print("A")
elif marks>=60:
    print("+B")
elif marks>=50:
    print("B")
elif marks>=45:
    print("C")
elif marks>=40:
    print("P")
else:
    print("F")
    