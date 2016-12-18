# Consider the following code:


def increment(n):
    n += 1
    # blank#
    return n

n = 1
while n < 10:
    n = increment(n)
print(n)

# Fill in the #blank# to ensure this prints 10.
