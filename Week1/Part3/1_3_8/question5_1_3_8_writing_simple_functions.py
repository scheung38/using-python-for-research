# http://stackoverflow.com/questions/5136447/function-for-factorial-in-python
def factorial(n):
    if n == 0:
        return 1
    else:
        N = 1
        for i in range(1, n + 1):
        # blank#
            N = n * factorial(n - 1)
            return N

        # Can you fill in the #blank# to complete the function
        # as described above?


print(factorial(5))


def factorial2(n):
    if n == 0:
        return 1
    else:
        return n * factorial2(n - 1)


# test =factorial2(5)
print(factorial2(5))

# was 7569
# now 7464.6

# was
# VAT = x * 0.145 = 7569
# x = 7569/0.145 = 52200

# now
# 0.145 * 51480 = 7464
