age = {'Jim': 31, 'Nick': 31, 'Pam': 27, 'Sam': 35, 'Tim': 31, 'Tom': 50}
print(age.keys())
# dict_keys(['Tim', 'Sam', 'Nick', 'Pam', 'Jim', 'Tom'])
print(age.values())
# dict_values([31, 31, 35, 27, 50, 31])

for name in age.keys():
    print(name, age[name])

print()

# Same as above
for name in age:
    print(name, age[name])

print()

for name in sorted(age):
    print(name, age[name])

print()

for name in sorted(age, reverse=True):
    print(name, age[name])

bears = {"Grizzly": "angry", "Brown": "friendly", "Polar": "friendly"}
print(bears.keys())
print(bears.values())
# replace #blank# so the code will print a greeting only to friendly bears?

for bear in bears:
    # print(type(bear))
    # if #blank#:
    # print(bear, bears[bear])

    if bears[bear] == 'friendly':
        print("Hello, " + bear + " bear!")
    else:
        print("odd")
