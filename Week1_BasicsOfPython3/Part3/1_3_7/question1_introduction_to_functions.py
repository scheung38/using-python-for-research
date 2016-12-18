def modify(mylist):
    mylist[0] *= 10
    return mylist

L = [1,3,7,9]
M = modify(L)
print(M is L)
# True