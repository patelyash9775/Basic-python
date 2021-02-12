f_name=input("Input the Filename : ")
f_extension=f_name.split(".")

if f_extension[-1]=='py':
    print("'python'")
elif f_extension[-1]=='cpp':
    print("'c++'")
else:
    print(repr(f_extension[-1]))



