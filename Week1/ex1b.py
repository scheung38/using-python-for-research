import string

alphabet = string.ascii_letters
sentence = 'Jim quickly realized that the beautiful gowns are expensive'

count_letters = {}
# write your code here!
count_letters = {i: sentence.count(i) for i in sentence if i in alphabet}
print(count_letters)
