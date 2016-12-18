is_prime = True
n = 8
for i in range(2, n):
    if n % i == 0:
        # blank #
        is_prime = False # answer

print(is_prime)
