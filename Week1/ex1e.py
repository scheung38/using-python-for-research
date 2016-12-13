# write your code here!
# What is the most common letter used in the Gettysburg Address?
# Store this letter as most_frequent_letter, and print your answer.
# address_count = counter(address)

from Week1.ex1c import counter
from Week1.ex1d import address_count

most_frequent_letter = max(address_count, key=address_count.get)

print(most_frequent_letter)