
a=list(map(int,input().split(",")))
l=[]

for i in range(len(a)):
    if(a[i]>0):
        l.append(a[i])
        
print(l)