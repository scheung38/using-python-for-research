L1 = [2, 3, 4]
M1 = L1
M2 = L1[:]

print(M1 is M2)
# False

# Same as above
print(id(M1) == id(M2))
# False