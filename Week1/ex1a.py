import string

alphabet = string.ascii_letters


def count_letter(input):
    alphabet = string.ascii_letters
    print(alphabet)
    return {i: input.count(i) for i in input if i in alphabet}


print(count_letter('Hello 123'))
