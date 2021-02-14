
a=[1,2,3,4,5]

def sample(*non_list,**s):
    total=0
    for i in non_list:
        total+=i
    return total

print(sample(*a))