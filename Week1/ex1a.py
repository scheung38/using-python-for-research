# In this five-part exercise, we will count the frequency of
# each letter in a given string.

# Instructions
# The lowercase and uppercase English alphabet can be found
# using ascii_letters attribute in the string library. Store
# this as alphabet.

# http://stackoverflow.com/questions/991350/counting-repeated-characters-in-a-string-in-python

import string

alphabet = string.ascii_letters


def counter(input):
    alphabet = string.ascii_letters
    print(alphabet)
    return {i: input.count(i) for i in input if i in alphabet}


print(counter("Hello 123"))

# def countLetters(word):
#     letterdict={}"StackExchange"
#     for letter in word:
#         letterdict[letter] = 0
#     for letter in word:
#         letterdict[letter] += 1
#     return letterdict

# print(myfunction())


# str = "StackExchange"
# print({i:str.count(i) for i in str})

# import string
# alphabet = string.ascii_letters
# sentence = 'Jim quickly realized that the beautiful gowns are expensive'
#
# count_letters = {}
# #write your code here!
# count_letters = {i: sentence.count(i) for i in sentence if i in alphabet}


# import string
# alphabet = string.ascii_letters
# sentence = 'Jim quickly realized that the beautiful gowns are expensive'
# # Create your function here!
# def counter(input_string):
#     return {i: input_string.count(i) for i in input_string if i in alphabet}
#
# counter(sentence)

address = "Four score and seven years ago our fathers brought forth on this continent a new nation, " \
          "conceived in liberty, and dedicated to the proposition that all men are created equal. " \
          "Now we are engaged in a great civil war, testing whether that nation, or any nation so " \
          "conceived and so dedicated, can long endure. We are met on a great battlefield of that war. " \
          "We have come to dedicate a portion of that field, as a final resting place for those who here " \
          "gave their lives that that nation might live. It is altogether fitting and proper that we should " \
          "do this. But, in a larger sense, we can not dedicate, we can not consecrate, we can not hallow " \
          "this ground. The brave men, living and dead, who struggled here, have consecrated it, far above " \
          "our poor power to add or detract. The world will little note, nor long remember what we say here, " \
          "but it can never forget what they did here. It is for us the living, rather, to be dedicated here " \
          "to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for " \
          "us to be here dedicated to the great task remaining before us—that from these honored dead we take " \
          "increased devotion to that cause for which they gave the last full measure of devotion—that we here " \
          "highly resolve that these dead shall not have died in vain—that this nation, under God, shall have a " \
          "new birth of freedom—and that government of the people, by the people, for the people, shall not perish " \
          "from the earth."

# Ex1d
address_count = counter(address)

# Ex1e
# What is the most common letter used in the Gettysburg Address?
# Store this letter as most_frequent_letter, and print your answer.
print('This is dictionary of address_count : %s' % address_count)


# http://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary

# Ex1e
address_count = counter(address)
most_frequent_letter = max(address_count, key=address_count.get)
print(most_frequent_letter)

