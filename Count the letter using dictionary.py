import operator

string=input("Please Enter a string: ")
s=list(string)


def counting(s):
    a={}
    b=[]
    for i in range(len(s)):
        if(s[i] not in b):
            a[str(s[i])]=s.count(s[i])
            b.append(s.count(s[i]))
    sorted_dict=dict(sorted(a.items(),key=operator.itemgetter(1),reverse=True))
    return sorted_dict
       
d=counting(s)       
for i in d:
    if(d[i]//10==0):
        print(i," = ",end="")
        print("0"+str(d[i]))
    else:
        print(i," = ",d[i])
        
        
