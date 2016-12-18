# Create a dictionary letters that maps each number from 0 to 26 to each character in alphabet.

# http://stackoverflow.com/questions/14902904/how-to-create-a-dict-with-letters-as-keys-in-a-concise-way
import string
string.ascii_lowercase

# We will consider the alphabet to be these letters, along with a space.
alphabet = string.ascii_lowercase + " "

# create `letters` here!
# print(len(alphabet))
print('Stackoverflow:')
# letters1 = {x: i for i, x in enumerate(alphabet, 1)}
letters1 = {i: x for i, x in enumerate(alphabet, 0)}
print(letters1)


# edX solution
print('edx Solution:')
letters2 = dict(enumerate(alphabet))
print(letters2)

print(letters1 == letters2)
# False
