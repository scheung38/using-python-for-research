# Consider the following proposed emendation of is_vowel :

def is_vowel(letter):
    if type(letter) == int:
        letter = str(letter)
    if letter in "aeiouy":
        return (True)
    else:
        return (False)

print(is_vowel(4))
# True