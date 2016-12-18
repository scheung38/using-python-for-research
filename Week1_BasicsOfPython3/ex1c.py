# Rewrite your code from 1b to make a function called counter that
# takes a string input_string and returns a dictionary of letter
# counts count_letters. If you were unable to complete 1b, you can
# use the solution by selecting Show Answer.

# Use your function to call counter(sentence).

import string

alphabet = string.ascii_letters
sentence = 'Jim quickly realized that the beautiful gowns are expensive'


def counter(input_string):
    return {i: input_string.count(i) for i in input_string if i in alphabet}

print(counter(sentence))

