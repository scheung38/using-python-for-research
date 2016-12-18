import string
string.ascii_lowercase

alphabet = string.ascii_lowercase + " "
letters = dict(enumerate(alphabet))

key = 3

# define `coded_message` here!
# coded_message = {x: i for i, x in enumerate(alphabet, key)}
# print(coded_message)

# this is correct but edX rejected

coded_message = {letter: (place + key) % 27 for (place, letter) in enumerate(alphabet)}

if __name__ == '__main__':
    print('coded_message is :')
    print(coded_message)

