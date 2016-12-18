# How can you use a list comprehension, including if and for,
# to sum the odd numbers from 0 through 9?


print(sum(i for i in range(10) if i < 9))
