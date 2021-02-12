n=int(input("Enter term where till we want to print series : "))
print("The fibonacci series till term ",n," : ",end=" ")

a=0
b=1
c=0
print(a,end=" ")
print(b,end=" ")

for i in range(0,n-2):
    c=a+b
    print(c,end=" ")
    a=b
    b=c
    
    